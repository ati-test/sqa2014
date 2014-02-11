# language: ru

Функционал: Проверка баннеров на сайты партнеров конференции

    Сценарий:
        Если зайти на сайт http://sqadays.com

    Структура сценария: проверяем, все ли баннеры в разделе "наши партнеры" работают корректно
        Если нажать на <баннер> партнера
        Тогда в соседнем окне откроется <сайт партнера>
        
    Примеры: партнеры конференции
        |баннер           |сайт партнера                        |
        |superjob         |http://www.superjob.ru/              |
        |it_sobytie       |http://www.it-sobytie.ru/            |
        |piterpy          |http://www.it-sobytie.ru/events/2040 |
        
        
    Примеры: информационные партнеры конференции 
        |баннер           |сайт партнера                        |
        |russoft          |http://www.russoft.ru/               |
        |softline         |http://softline.ru/                  |
        |cnews            |http://www.cnews.ru/                 |
        |testers_life     |http://www.testers-life.ru/          |
        