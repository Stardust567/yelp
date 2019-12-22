# yelp

`tree`

.
├── MapPlot.py
├── README.md
├── data
│   ├── dataMap.csv
│   ├── dataMat.csv
│   ├── display.py
│   └── processed.csv
├── dataMap.py
├── dataPlot.py
├── dataProcessing.py
├── linePicture
│   ├── ATXCocina.png
│   ├── AboYoussef.png
│   ├── Anthem.png
│   ├── ...
├── requirements.txt
├── rotate_azimuth_angle_3d_surf.mp4
├── scrapy.cfg
├── streetMap.py
├── test.csv
├── yelp
│   ├── __init__.py
│   ├── __pycache__
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
├── yelpAustin.html
└── yelpNLP.py

5 directories, 180 files

## Crawler

This is the **Web Crawler** part used Scrapy to scrape yelp review about stores & shops in Austin from https://www.yelp.com/ .

You can enter `pip install -r requirements.txt` in cmd/shell to make sure you have installed all the requirements.

### Extracted data

This project extracts information, combined with address, time, name and review. The extracted data looks like this sample:
{
 "address": "7301 Burnet Rd Ste 101  Austin, TX 78757 ",
 "time": "         7/14/2019       ",
 "name": "DipDipDip Tatsu-Ya",
 "review": "For me the  food was okay but too expensive. The main disappointment...",
}

> The part of review in each data contains reviews in this shop about approximate three month.

### Spiders

This project contains two spiders and you can list them using the list command:

```shell
$ scrapy list
```

> Review

You can learn more about using **Scrapy** by going through [my blog](https://stardust567.github.io/post/b2a.html).

### Running the spiders

You can run a spider using the scrapy crawl command, such as:

```powershell
$ scrapy crawl Review
```