# @bash
crypto, 50 points

> Расшифруйте секретное послание: `ZnhndV9nc3pnX3hpYmtnbF9kemhfdnpoYg==`

*Hint* (-25): В России @ — собака. А как в Англии?

## Write-up

Сначала base64, это вполне очевидно.

Далее смотрим на название: `@` = `at`, значит, шифр — Атбаш. Получаем флаг.

Флаг: **uctf_that_crypto_was_easy**
