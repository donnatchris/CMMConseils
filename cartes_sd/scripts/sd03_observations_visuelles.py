#!/usr/bin/env python3
"""Consigne les images effectivement examinées par l'assistant dans cette campagne.
Dates lues visuellement ; aucun OCR ni identification des personnes.
"""
import hashlib,json
from sd03_collect import OUT
seen=[
('prive/apercus/714049800-0.png','2024-10-15 13:28:00'),('prive/apercus/714049800-138.88.png','2024-10-15 13:30:21'),('prive/apercus/714049796-0.png','2024-10-15 13:26:34'),('prive/apercus/714049796-74.928.png','2024-10-15 13:27:49'),
('prive/apercus/12727332-0.png','2023-11-09 18:19:05'),('prive/apercus/261989424-0.png','2024-02-21 23:22:37'),('prive/apercus/261989436-0.png','2024-02-21 23:33:44'),('prive/apercus/261989444-0.png','2024-02-21 23:41:03'),
('prive/apercus/266341920-0.png','2024-02-29 10:26:10'),('prive/apercus/266341968-0.png','2024-02-29 10:56:00'),('prive/apercus/266341984-0.png','2024-02-29 11:01:38'),('prive/apercus/266342024-0.png','2024-02-29 11:27:24'),
('prive/derniers-apercus/714049800.png','2024-10-15 13:32:26'),('prive/derniers-apercus/261989424.png','2024-02-21 23:25:46'),('prive/derniers-apercus/261989436.png','2024-02-21 23:34:58'),('prive/derniers-apercus/261989444.png','2024-02-21 23:41:44'),('prive/derniers-apercus/12727332.png','2023-11-09 18:19:43'),
('prive/derniers-apercus/266341920.png','2024-02-29 10:26:57'),('prive/derniers-apercus/266341968.png','2024-02-29 10:56:01'),('prive/derniers-apercus/266341984.png','2024-02-29 11:03:32'),('prive/derniers-apercus/266342024.png','2024-02-29 11:27:40'),('prive/apercus-eof/0.png','2024-02-29 11:27:41'),('prive/apercus-eof/3.349.png','2024-02-29 11:27:45')]
observations=[dict(artifact=name,sha256=hashlib.sha256((OUT/name).read_bytes()).hexdigest(),overlay_read_visually=date) for name,date in seen]
result=dict(method='Examen visuel par l’assistant de 23 PNG extraits dans SIFT ; pas un visionnage humain intégral, pas une lecture OCR',observations=observations,scope='Incrustations de dates, présence de personnes et changements de cadrage seulement ; aucun rôle, identité, accès distant ou geste de reset n’est attribué.',critical='Les aperçus du 15 octobre montrent plusieurs personnes et des documents dans le salon, puis un cadrage différent et une image floue proche de la dernière PTS. Ils ne permettent pas d’identifier une commande, un retrait de carte ou une coupure d’alimentation.',limits='Dates de caméra non étalonnées ; temps demandés d’extraction approximatifs en présence d’index abîmés ; absence de bascule vers 2000 dans ces images échantillonnées ne garantit pas une absence de changement entre celles-ci.')
with (OUT/'inventaires/observations-visuelles.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(len(observations),'images effectivement examinées')
