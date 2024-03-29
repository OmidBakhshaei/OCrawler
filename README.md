# OCrawler


OCrawler is a web crawler built with Python using [_Scrapy_](https://scrapy.org/) package.
It crawls a Web page, extracts all URLs contained within the page, and saves them to a CSV file.

---

## Usage
1. make sure that Scrapy is installed:


    ```
    pip install Scrapy
    ```

2. Open the [OCrawler.py](/CR/CR/spiders/OCrawler.py) in your editor and change the _start_urls_ variable to the desired URL.

    (It is now set on https://video.varzesh3.com.)

    ``` python
    start_urls = ['https://video.varzesh3.com/']
    ```

3. Run the code.

4. Copy and paste the **scrapy crawl link_checker** command to your command line to start the crawler.

5. Copy and paste the **scrapy crawl link_checker -o link_checker.csv** command to save the output in a CSV file in the same directory of the Python file.


---

Here is an example of the output of a crawled website ([video.varzesh3.com](https://video.varzesh3.com)) by OCrawler.


|text                                                                                |link                                                                         |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|                                                                                    |/syv                                                                         |
|                                                                                    |/login?redirect=http://video.varzesh3.com/                                   |
|ورزش سه                                                                             |http://www.varzesh3.com/                                                     |
|صفحه اصلی                                                                           |http://video.varzesh3.com/                                                   |
|راهنمای سایت                                                                        |/help/                                                                       |
|تماس با ما                                                                          |/contact                                                                     |
|                                                                                    |/                                                                            |
|ایران                                                                               |/category/iran                                                               |
|لیگ برتر                                                                            |/category/iran/premier-league                                                |
|جام حذفی                                                                            |/category/iran/jam-hazfi                                                     |
|لیگ 1                                                                               |/category/iran/leagu-1                                                       |
|آلمان                                                                               |/category/germany                                                            |
|بوندسلیگا                                                                           |/category/germany/bundesliga                                                 |
|جام حذفی                                                                            |/category/germany/جام-حذفی-germany                                           |
|اسپانیا                                                                             |/category/spain                                                              |
|لالیگا                                                                              |/category/spain/la-liga                                                      |
|کوپا دل ری                                                                          |/category/spain/copa_del_rey                                                 |
|انگلیس                                                                              |/category/england                                                            |
|لیگ برتر جزیره                                                                      |/category/england/premier-league-england                                     |
|جام حذفی                                                                            |/category/england/fa-cup                                                     |
|جام اتحادیه                                                                         |/category/england/carlling_cup                                               |
|ایتالیا                                                                             |/category/italia                                                             |
|سری آ                                                                               |/category/italia/calcio-serie-a                                              |
|کوپا ایتالیا                                                                        |/category/italia/coppa-italia                                                |
|فرانسه                                                                              |/category/france                                                             |
|لوشامپیونه                                                                          |/category/france/loshampioneh                                                |
|جام حذفی                                                                            |/category/france/hazfi                                                       |
|جام باشگاه ها                                                                       |/category/champions-league                                                   |
|لیگ قهرمانان اروپا                                                                  |/category/champions-league/champions                                         |
|یورو لیگ                                                                            |/category/champions-league/europa-league                                     |
|لیگ قهرمانان اسیا                                                                   |/category/champions-league/afc-cup                                           |
|باشگاه های جهان                                                                     |/category/champions-league/club_worldcup                                     |
|بین المللی                                                                          |/category/international                                                      |
|جام جهانی                                                                           |/category/international/world-cup                                            |
|2014 برزیل                                                                          |/category/international/world-cup/2014-brazil                                |
|فوتسال 2012                                                                         |/category/international/world-cup/futsal_2012                                |
|جام ملتهای اروپا                                                                    |/category/international/uefa-cup-europe                                      |
|2012                                                                                |/category/international/uefa-cup-europe/2012                                 |
|یورو 2016                                                                           |/category/international/uefa-cup-europe/UEFA-Euro-2016                       |
|جام ملتهای آسیا                                                                     |/category/international/afc-asian-cup                                        |
|2019                                                                                |/category/international/afc-asian-cup/asia19                                 |
|2015                                                                                |/category/international/afc-asian-cup/2015                                   |
|جام ملتهای آفریقا                                                                   |/category/international/africa-cup-of-nations                                |
|2013                                                                                |/category/international/africa-cup-of-nations/2013                           |
|کوپا آمریکا                                                                         |/category/international/copa                                                 |
|بازی های دوستانه                                                                    |/category/international/friendly_games                                       |
|المپیک                                                                              |/category/international/olympics                                             |
|لندن 2012                                                                           |/category/international/olympics/london_2012                                 |
|سایر لیگها                                                                          |/category/international/other-international                                  |
|بازيهاي آسيايي                                                                      |/category/international/asian-games                                          |
|کونکاکاف                                                                            |/category/international/concacaf                                             |
|سایر ورزش ها                                                                        |/category/other-video-clips                                                  |
|والیبال                                                                             |/category/other-video-clips/valleyball                                       |
|بسکتبال                                                                             |/category/other-video-clips/basketball                                       |
|سایر رشته ها                                                                        |/category/other-video-clips/other_sport                                      |
|کشتی                                                                                |/category/other-video-clips/wrestling                                        |
|فوتسال                                                                              |/category/other-video-clips/futsal                                           |
|ویدئو کلیپ                                                                          |/category/video-clips                                                        |
|آنالیز                                                                              |/category/video-clips/آنالیز                                                 |
|سکانس برتر                                                                          |/category/video-clips/bartar                                                 |
|سیوهای برتر                                                                         |/category/video-clips/سیوهای برتر                                            |
|ویدیو نوشت                                                                          |/category/video-clips/videotext                                              |
|مصاحبه اختصاصی                                                                      |/category/video-clips/Interview                                              |
|فوتبالیستها                                                                         |/category/video-clips/fotbalistha                                            |
|زیرنویس فارسی                                                                       |/category/video-clips/persian-subtitles                                      |
|بهترین بازیکن ماه                                                                   |/category/video-clips/best                                                   |
|برنامه نود                                                                          |/category/video-clips/90pro                                                  |
|حواشی                                                                               |/category/video-clips/margins                                                |
|سرگرمی                                                                              |/category/video-clips/fun                                                    |
|نمایشی                                                                              |/category/video-clips/technical_movements                                    |
|برترین های هفته                                                                     |/category/video-clips/goal-week                                              |
|بازیکنان                                                                            |/category/video-clips/players                                                |
|آموزشی                                                                              |/category/video-clips/learning                                               |
|گلهای  برتر                                                                         |/category/video-clips/best_goals                                             |
|خاطره انگیزها                                                                       |/category/video-clips/nostalgia                                              |
|بازی خور                                                                            |/category/video-clips/gamer                                                  |
|دوربین مردمی                                                                        |/category/video-clips/ucamera                                                |
|اخبار                                                                               |/category/video-clips/news                                                   |
|کلیپ ثانیه ای                                                                       |/category/video-clips/short-clip                                             |
|عملکرد بازیکن                                                                       |/category/video-clips/vs                                                     |
|تکنیک ها و مهارتها                                                                  |/category/video-clips/skills                                                 |
|نتایج زنده                                                                          |http://www.varzesh3.com/livescore                                            |
|                                                                                    |/video/222205/حضور-ملی-پوشان-با-هلی‌کوپتر-به-آزادی-پس-از-صعود-به-جام-جهانی-98|
|                                                                                    |/video/222204/خلاصه-بازی-اسلاویاپراگ-1-بایر-لورکوزن-0                        |
|                                                                                    |/video/222203/خلاصه-بازی-رئال-سوسیداد-0-ناپولی-1                             |
|                                                                                    |/video/222202/خلاصه-بازی-آ-اس-رم-0-زسکاصوفیه-0                               |
|                                                                                    |/video/222201/تمرینات-آماده-سازی-بازیکنان-بارسلونا-برای-دیدار-با-آلاوس       |
|                                                                                    |/video/222200/خلاصه-بازی-آرسنال-3-دانداک-0-(گزارش-اختصاصی)                   |
|                                                                                    |/video/222199/گل-سوم-آرسنال-به-دانداک-با-سوپر-گل-په-په                       |
|                                                                                    |/video/222198/گل-دوم-آرسنال-به-دانداک-توسط-ویلوک                             |
|                                                                                    |/video/222197/گل-اول-آرسنال-به-دانداک-توسط-انکتیا                            |
|                                                                                    |/video/222184/5-گل-برتر-مونشن-گلادباخ-برابر-لایپزیش                          |
|                                                                                    |/video/222195/خلاصه-بازی-آنتورپ-1-تاتنهام-0                                  |
|                                                                                    |/video/222196/خلاصه-بازی-آث-میلان-3-اسپارتاپراگ-0                            |
|                                                                                    |/video/222194/خلاصه-بازی-آاک-1-لسترسیتی-2-(گزارش-اختصاصی)                    |
|                                                                                    |/video/222193/گل-سوم-آث-میلان-به-اسپارتاپراگ-(-دالوت)                        |
|                                                                                    |/video/222188/5-گل-برتر-دیگو-مارادونا-در-تاریخ-جام-جهانی                     |
|                                                                                    |/video/222192/گل-دوم-آث-میلان-به-اسپارتاپراگ-(-لیائو)                        |
|                                                                                    |/video/222191/گل-اول-آث-میلان-به-اسپارتاپراگ-(-براهیم-دیاز-)                 |
|                                                                                    |/video/222190/10-سیو-برتر-ادوین-فن-در-سار-در-آژاکس-آمستردام                  |
|                                                                                    |/video/222187/سوپرگل-های-آ-اس-رم-با-لباس-مشکی-این-تیم                        |
|                                                                                    |/video/222186/29-اکتبر-روز-جهانی-مربی                                        |
|                                                                                    |/video/222119/مدافعانی-که-هرگز-مسی-را-فراموش-نخواهند-کرد                     |
|                                                                                    |/video/222185/جعفر-سمیعی-مدیرعامل-باشگاه-پرسپولیس-شد                         |
|                                                                                    |/video/222183/آخرین-تمرینات-تاتنهام-برای-دیدار-برابر-آنتورپ                  |
|                                                                                    |/video/222181/مصاحبه-اختصاصی-و-کامل-با-احمد-موسوی-بازیکن-جدید-استقلال        |
|1                                                                                   |/api/video/#1                                                                |
|2                                                                                   |/api/video/#2                                                                |
|3                                                                                   |/api/video/#3                                                                |
|4                                                                                   |/api/video/#4                                                                |
|                                                                                    |/video/221960/خلاصه-بازی-بارسلونا-1-رئال-مادرید-3-(گزارش-اختصاصی)            |
|                                                                                    |/video/222159/خلاصه-بازی-یوونتوس-0-بارسلونا-2                                |
|                                                                                    |/video/222002/سوپرگل-سه-امتیازی-رامین-رضاییان-برای-الدحیل                    |
|                                                                                    |/video/222100/خلاصه-بازی-مونشن-گلادباخ-2-رئال-مادرید-2                       |
|                                                                                    |/video/222160/خلاصه-بازی-منچستریونایتد-5-لایپزیش-0                           |
|                                                                                    |/video/221959/گل-سوم-رئال-مادرید-به-بارسلونا-توسط-مودریچ                     |
|                                                                                    |/video/222050/خلاصه-بازی-میلان-3-آاس-رم-3                                    |
|                                                                                    |/video/222148/گل-اول-بارسلونا-به-یوونتوس-توسط-دمبله                          |
|                                                                                    |/video/221958/گل-دوم-رئال-مادرید-به-بارسلونا-(پنالتی-راموس)                  |
|                                                                                    |/video/221974/مصدومیتی-که-دنیای-فوتبال-را-به-کما-برد-!                       |
|                                                                                    |/video/221911/صحبت-های-نیکبخت-پس-از-پیوستن-محمد-نادری-به-استقلال             |
|                                                                                    |/video/222004/اولین-گل-الهیار-صیادمنش-برای-زوریا                             |
| سوپرگل روفی و گل دوم رنجرز به استاندارد لیژ                                        |/video/221883/سوپرگل-روفی-و-گل-دوم-رنجرز-به-استاندارد-لیژ                    |
| گل از راه دور زیبا پوگبا به اودینزه با پیراهن یوونتوس                              |/video/214754/گل-از-راه-دور-زیبا-پوگبا-به-اودینزه-با-پیراهن-یوونتوس          |
| مهار تماشایی پنالتی سامان قدوس توسط رشید مظاهری                                    |/video/221477/مهار-تماشایی-پنالتی-سامان-قدوس-توسط-رشید-مظاهری                |
| آنسو فاتی در نقش عکاس تیم ملی اسپانیا                                              |/video/221461/آنسو-فاتی-در-نقش-عکاس-تیم-ملی-اسپانیا                          |
| وقتی بشار رسن به دعوت عبدی مازنی حرف می‌زند!                                       |/video/221370/وقتی-بشار-رسن-به-دعوت-عبدی-مازنی-حرف-می‌زند!                   |
| ورود عکاشه حمزویی به تبریز                                                         |/video/221368/ورود-عکاشه-حمزویی-به-تبریز                                     |
| تایید بهمن نیکخو در خصوص سرمربیگری فکری                                            |/video/221089/تایید-بهمن-نیکخو-در-خصوص-سرمربیگری-فکری                        |
| اشک های سوارز در نشست خبری خداحافظی بارسلونا                                       |/video/220531/اشک-های-سوارز-در-نشست-خبری-خداحافظی-بارسلونا                   |
| گزارشگر الکاس در حال گزارش بازی پرسپولیس و التعاون                                 |/video/220306/گزارشگر-الکاس-در-حال-گزارش-بازی-پرسپولیس-و-التعاون             |
| عالیشاه: افتخار میکنم اگر در پرسپولیس بمانم                                        |/video/219883/عالیشاه-افتخار-میکنم-اگر-در-پرسپولیس-بمانم                     |
|                                                                                    |/video/222204/خلاصه-بازی-اسلاویاپراگ-1-بایر-لورکوزن-0                        |
|                                                                                    |/video/222203/خلاصه-بازی-رئال-سوسیداد-0-ناپولی-1                             |
|                                                                                    |/video/222202/خلاصه-بازی-آ-اس-رم-0-زسکاصوفیه-0                               |
|                                                                                    |/video/222200/خلاصه-بازی-آرسنال-3-دانداک-0-(گزارش-اختصاصی)                   |
|                                                                                    |/video/222195/خلاصه-بازی-آنتورپ-1-تاتنهام-0                                  |
|                                                                                    |/video/222196/خلاصه-بازی-آث-میلان-3-اسپارتاپراگ-0                            |
|                                                                                    |/video/222194/خلاصه-بازی-آاک-1-لسترسیتی-2-(گزارش-اختصاصی)                    |
|                                                                                    |/video/222161/خلاصه-بازی-کلوب-بروژ-1-لاتزیو-1                                |
|                                                                                    |/video/222160/خلاصه-بازی-منچستریونایتد-5-لایپزیش-0                           |
|                                                                                    |/video/222158/خلاصه-بازی-سویا-1-رن-0                                         |
|                                                                                    |/video/222159/خلاصه-بازی-یوونتوس-0-بارسلونا-2                                |
|                                                                                    |/video/222155/خلاصه-بازی-دورتموند-2-زنیت-0-(گزارش-اختصاصی)                   |
|                                                                                    |/video/222149/خلاصه-بازی-کراسنودار-0-چلسی-4                                  |
|                                                                                    |/video/222147/خلاصه-بازی-باشاک-شهیر-0-پاری-سن-ژرمن-2-(گزارش-اختصاصی)         |
|                                                                                    |/video/222103/خلاصه-بازی-پورتو-2-المپیاکوس-0                                 |
|                                                                                    |/video/222102/خلاصه-بازی-آتالانتا-2-آژاکس-2                                  |
|                                                                                    |/video/222101/خلاصه-بازی-اتلتیکومادرید-3-سالزبورگ-2                          |
|                                                                                    |/video/222100/خلاصه-بازی-مونشن-گلادباخ-2-رئال-مادرید-2                       |
|                                                                                    |/video/222099/خلاصه-بازی-مارسی-0-منچسترسیتی-3                                |
|                                                                                    |/video/222096/خلاصه-بازی-لیورپول-2-میتیلند-0                                 |
|                                                                                    |/video/222090/خلاصه-بازی-شاختار-0-اینتر-0                                    |
|                                                                                    |/video/222089/خلاصه-بازی-لوکوموتیو-موسکو-1-بایرن-مونیخ-2                     |
|                                                                                    |/video/222050/خلاصه-بازی-میلان-3-آاس-رم-3                                    |
|                                                                                    |/video/222041/خلاصه-بازی-دوستانه-پرسپولیس-ملوان                              |
|                                                                                    |/video/222008/خلاصه-بازی-یوونتوس-1-هلاس-ورونا-1                              |
|                                                                                    |/video/222007/خلاصه-بازی-آرسنال-0-لسترسیتی-1                                 |
|                                                                                    |/video/221999/خلاصه-بازی-بنونتو-1-ناپولی-2                                   |
|                                                                                    |/video/221997/خلاصه-بازی-ساوتهمپتون-2-اورتون-0-(گزارش-اختصاصی)               |
|                                                                                    |/video/221978/خلاصه-بازی-اتلتیکو-مادرید-2-رئال-بتیس-0                        |
|                                                                                    |/video/221977/خلاصه-بازی-لیورپول-2-شفیلدیونایتد-1                            |
|                                                                                    |/video/221976/خلاصه-بازی-پاری-سن-ژرمن-4-دیژون-0                              |
|                                                                                    |/video/221975/خلاصه-بازی-لاتزیو-2-بولونیا-1                                  |
|                                                                                    |/video/221971/خلاصه-بازی-جنوا-0-اینتر-2                                      |
|                                                                                    |/video/221968/خلاصه-بازی-منچستریونایتد-0-چلسی-0                              |
|                                                                                    |/video/221967/خلاصه-بازی-دورتموند-3-شالکه-0-(گزارش-اختصاصی)                  |
| برترین گلهای بارسلونا در مقابل یوونتوس                                             |/video/222127/برترین-گلهای-بارسلونا-در-مقابل-یوونتوس                         |
| سوپرگل های تاریخ لیگ برتر جزیره در این هفته                                        |/video/222123/سوپرگل-های-تاریخ-لیگ-برتر-جزیره-در-این-هفته                    |
| حرکت های دیدنی زلاتان ابراهیموویچ در حین بازی                                      |/video/221597/حرکت-های-دیدنی-زلاتان-ابراهیموویچ-در-حین-بازی                  |
| برترین گلهای رائول گونزالس در رئال مادرید                                          |/video/221985/برترین-گلهای-رائول-گونزالس-در-رئال-مادرید                      |
| بارسلونا - رئال مادرید؛ نبرد دو غول لالیگا بدون حضور تماشاگران                     |/video/221941/بارسلونا-رئال-مادرید؛-نبرد-دو-غول-لالیگا-بدون-حضور-تماشاگران   |
| گلهای ناجوانمردانه تاریخ فوتبال جهان                                               |/video/198344/گلهای-ناجوانمردانه-تاریخ-فوتبال-جهان                           |
| 10 گل برتر اینتر در مقابل آث میلان                                                 |/video/221633/10-گل-برتر-اینتر-در-مقابل-آث-میلان                             |
| 10 گل از راه خیلی دور و جالب در حین بازی                                           |/video/221724/10-گل-از-راه-خیلی-دور-و-جالب-در-حین-بازی                       |
| 14 گل تماشایی از نابغه فوتبال جهان کریستیانو رونالدو                               |/video/219218/14-گل-تماشایی-از-نابغه-فوتبال-جهان-کریستیانو-رونالدو           |
| مسی - مارادونا - پله; بهترین کیست؟                                                 |/video/146575/مسی-مارادونا-پله;-بهترین-کیست؟                                 |
|                                                                                    |#scroll-to-top                                                               |
|                                                                                    |https://facebook.com/varzesh3                                                |
|                                                                                    |https://www.instagram.com/varzesh3/                                          |
|                                                                                    |https://twitter.com/varzesh3                                                 |
|                                                                                    |/rss                                                                         |
|قوانین                                                                              |http://www.varzesh3.com/policy                                               |
|ابزار توسعه                                                                         |http://www.varzesh3.com/dev                                                  |
|جداول لیگ ها                                                                        |http://www.varzesh3.com/table                                                |
|راهنمای سایت                                                                        |/help                                                                        |
|تماس با ما                                                                          |/contact                                                                     |
|صفحه اصلی                                                                           |http://video.varzesh3.com/                                                   |
|ورزش سه                                                                             |http://www.varzesh3.com/                                                     |
|"سرویس ویدیو ورزش سه"                                                               |/                                                                            |
