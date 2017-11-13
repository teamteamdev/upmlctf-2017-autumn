# Pretty
stegano, 100 points

> Какой умилительный котик!

[Вложение](very-pretty.png)

*Hint* (-40): Найди оригинал картинки	

## Write-up
Ищем оригинал, оригиналов предостаточно. [Пример](https://pbs.twimg.com/media/DHchVAGXgAENSM8.jpg).

Сравниваем с помощью stegsolve (Analyze → Image Combiner). Тут два варианта:

1. Режим XOR, сохранить и обнаружить, что есть буквы, которые написаны не черным, а близким к черному цветом
2. Режим SUB, флаг достаточно неплохо видно

Флаг: **uctf_it_s_stego_time**
