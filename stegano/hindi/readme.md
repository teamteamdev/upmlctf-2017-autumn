# Foreign
stegano, 100 points

> Наши спецслужбы перехватили сообщение подозрительного содержания. Что же хотел сказать его автор на самом деле?

[Вложение](hindi.enc)

*Hint* (0): это больше не стегано, а крипта

*Hint* (-65): [itsecwiki.org](http://itsecwiki.org)

## Write-up

Пробуем для начала Google-переводчик, получаем интересную мудрость, по уровню похожую на [@smorcbot](https://t.me/smorcbot) из чата #ctfdev из тасков Bad developer {1,2}.

Ищем шифр / метод скрытия информации в Хинди. Находим на [itsecwiki.org](http://itsecwiki.org/) в разделе String crypto алгоритм HINDIA-4X.

Так же по запросу вида `hindi indian crypto decrypter` можно нагуглить [сайт](http://temp.crypo.com/hindia-4x.htm), где есть декодер.

Флаг: **uctf_googletranslate_cant_solve_stego**