import pandas as pd, json
d=pd.read_csv('dados/eleitos.csv',sep=';',decimal=',',dtype=str,encoding='utf-8-sig')
d['idade']=pd.to_numeric(d.idade_posse_2025)
d['bens']=pd.to_numeric(d.bens_declarados_total_reais.str.replace(',','.'),errors='coerce')
p=d[d.cargo=='Prefeito'].copy(); v=d[d.cargo=='Vice-prefeito'].copy()
def prof(x):
    r=x.raca_cor_autodeclarada
    return dict(n=len(x),
      mulher=round(100*(x.genero_tse=='FEMININO').mean(),1),
      branca=round(100*(r=='BRANCA').mean(),1),
      negra=round(100*r.isin(['PARDA','PRETA']).mean(),1),
      parda=round(100*(r=='PARDA').mean(),1), preta=round(100*(r=='PRETA').mean(),1),
      superior=round(100*(x.escolaridade=='SUPERIOR COMPLETO').mean(),1),
      casado=round(100*(x.estado_civil=='CASADO(A)').mean(),1),
      reeleicao=round(100*(x.candidato_a_reeleicao_tse=='Sim').mean(),1),
      idade=int(x.idade.median()),
      menos40=round(100*(x.idade<40).mean(),1),
      bens=int(x.bens.median()))
out={'brasil':prof(p),'vice':prof(v)}
out['regiao']={k:prof(g) for k,g in p.groupby('regiao')}
out['uf']={k:dict(prof(g),nome=g.uf_nome.iloc[0],regiao=g.regiao.iloc[0]) for k,g in p.groupby('uf')}
# funnel
f=p; steps=[('Todos os prefeitos',len(f))]
f=f[f.genero_tse=='MASCULINO']; steps.append(('são homens',len(f)))
f=f[f.raca_cor_autodeclarada=='BRANCA']; steps.append(('… e brancos',len(f)))
f=f[f.escolaridade=='SUPERIOR COMPLETO']; steps.append(('… com curso superior',len(f)))
f=f[f.estado_civil=='CASADO(A)']; steps.append(('… e casados',len(f)))
out['funil']=steps
# women of color
out['mulher_negra']=int(((p.genero_tse=='FEMININO')&p.raca_cor_autodeclarada.isin(['PARDA','PRETA'])).sum())
out['mulher_preta']=int(((p.genero_tse=='FEMININO')&(p.raca_cor_autodeclarada=='PRETA')).sum())
# age bins
bins=[18,30,40,50,60,70,100]; lab=['até 29','30–39','40–49','50–59','60–69','70+']
out['idade_faixas']=dict(zip(lab,pd.cut(p.idade,bins,right=False,labels=lab).value_counts().reindex(lab).tolist()))
out['jovem']=p.idade.min(); out['velho']=p.idade.max()
# occupations
oc=p.ocupacao_declarada.value_counts()
out['ocup']=oc.head(10).to_dict()
# escolaridade
order=['LÊ E ESCREVE','ENSINO FUNDAMENTAL INCOMPLETO','ENSINO FUNDAMENTAL COMPLETO','ENSINO MÉDIO INCOMPLETO','ENSINO MÉDIO COMPLETO','SUPERIOR INCOMPLETO','SUPERIOR COMPLETO']
out['escol']=p.escolaridade.value_counts().reindex(order).fillna(0).astype(int).to_dict()
out['raca_na']=int(p.raca_cor_autodeclarada.isna().sum())
out['bens_na']=int(p.bens.isna().sum())
# chapa composition
ch=p[['id_chapa','genero_tse']].merge(v[['id_chapa','genero_tse']],on='id_chapa',suffixes=('_p','_v'))
out['chapa_gen']=ch.groupby(['genero_tse_p','genero_tse_v']).size().to_dict()
out['chapa_gen']={f'{a}-{b}':int(c) for (a,b),c in out['chapa_gen'].items()}
# women by city size proxy: votos validos municipio
p['vm']=pd.to_numeric(p.votos_validos_municipio_turno_atual_tse)
out['porte']={}
for lo,hi,l in [(0,5000,'até 5 mil votos'),(5000,20000,'5 a 20 mil'),(20000,100000,'20 a 100 mil'),(100000,1e9,'mais de 100 mil')]:
    g=p[(p.vm>=lo)&(p.vm<hi)]; out['porte'][l]=prof(g)
json.dump(out,open('agg.json','w'),ensure_ascii=False,indent=1,default=int)
print(json.dumps({k:out[k] for k in out if k!='uf'},ensure_ascii=False,indent=0,default=int))
