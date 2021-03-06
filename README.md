# Погода из терминала

Учебная задача в рамках модуля "API веб-сервисов — Урок 1. Получите погоду из терминала" для учебной платформы [dvmn.org](https://dvmn.org)

Скрипт получает погоду с сайта [wttr.in](https://wttr.in) на три дня для разных городов и выводит результат в консоль. 

# Подготовка к использованию

Для запуска необходимо следующее:
- Установленный Python 3
- Установлены зависимости командой 
```commandline
pip install -r requirements.txt
```

# Использование

Для запуска скрипта необходимо воспользоваться командой:
```commandline
python3 weather.py 
```

### Пример вывода

```commandline
$ python3 .\weather.py
```
```Прогноз погоды: London

                Пасмурно
       .--.     +12(10) °C
    .-(    ).   ↗ 26 km/h
   (___.__)__)  10 km
                0.0 mm
                        ┌─────────────┐
┌───────────────────────┤ Вт. 08 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│               Облачно        │
│  _ /"".-.     +12(10) °C     │      .--.     +11(9) °C      │
│    \_(   ).   ↗ 20-24 km/h   │   .-(    ).   ↗ 18-25 km/h   │
│    /(___(__)  10 km          │  (___.__)__)  10 km          │
│               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Ср. 09 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │  _`/"".-.     Небольшой ливн…│
│      .--.     +11(9) °C      │   ,\_(   ).   10 °C          │
│   .-(    ).   ↗ 14-19 km/h   │    /(___(__)  ↗ 3-4 km/h     │
│  (___.__)__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │
│               0.0 mm | 0%    │     ‘ ‘ ‘ ‘   0.4 mm | 84%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Чт. 10 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │     \   /     Ясно           │
│      .--.     +7(4) °C       │      .-.      +4(1) °C       │
│   .-(    ).   → 14-17 km/h   │   ― (   ) ―   → 13-18 km/h   │
│  (___.__)__)  10 km          │      `-’      10 km          │
│               0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
Местоположение: London [51.509648,-0.099076]

Все новые фичи публикуются здесь: @igor_chubin

Прогноз погоды: svo

                Пасмурно
       .--.     +1(-3) °C
    .-(    ).   ↑ 19 km/h
   (___.__)__)  10 km
                0.0 mm
                        ┌─────────────┐
┌───────────────────────┤ Вт. 08 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Пасмурно       │  _`/"".-.     Небольшой ливн…│
│      .--.     +1(-3) °C      │   ,\_(   ).   -2(-7) °C      │
│   .-(    ).   ↑ 13-18 km/h   │    /(___(__)  ↗ 13-19 km/h   │
│  (___.__)__)  10 km          │      *  *  *  10 km          │
│               0.0 mm | 0%    │     *  *  *   0.1 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Ср. 09 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│      .-.      Сильный снег   │
│  _ /"".-.     -4(-8) °C      │     (   ).    -2(-6) °C      │
│    \_(   ).   ↗ 11-14 km/h   │    (___(__)   ↗ 12-18 km/h   │
│    /(___(__)  10 km          │    * * * *    2 km           │
│               0.0 mm | 0%    │   * * * *     0.3 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐
┌───────────────────────┤ Чт. 10 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Сильный снег   │               Облачно        │
│     (   ).    +1(-4) °C      │      .--.     -4(-9) °C      │
│    (___(__)   ↗ 18-26 km/h   │   .-(    ).   → 14-25 km/h   │
│    * * * *    2 km           │  (___.__)__)  10 km          │
│   * * * *     0.4 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
Местоположение: Международный аэропорт Шереметьево, Шереметьевское шоссе, Московская область, ЦФО, 141426, РФ [55.9733219,37.4147891584969]

Все новые фичи публикуются здесь: @igor_chubin

Прогноз погоды: Череповец

   _`/"".-.     Небольшой снег
    ,\_(   ).   0(-4) °C
     /(___(__)  ↑ 16 km/h
       *  *  *  10 km
      *  *  *   0.0 mm
                        ┌─────────────┐
┌───────────────────────┤ Вт. 08 февр.├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Небольшой снег │      .-.      Умеренный снег │
│   ,\_(   ).   0(-4) °C       │     (   ).    -3(-7) °C      │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Сильный снег   │               Пасмурно       │
│     (   ).    -1(-5) °C      │      .--.     -3(-8) °C      │
│    (___(__)   ↑ 14-18 km/h   │   .-(    ).   ↗ 15-24 km/h   │
│    * * * *    2 km           │  (___.__)__)  10 km          │
│   * * * *     0.8 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
Местоположение: Череповец, городской округ Череповец, Вологодская область, Северо-Западный федеральный округ, 162600, РФ [59.1286965,37.9163892]

Все новые фичи публикуются здесь: @igor_chubin
```
