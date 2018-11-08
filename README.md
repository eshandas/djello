# Djello
A pretty and configurable admin panel to enhance the default Django Admin Panel based on [Ela Admin](https://github.com/puikinsh/ElaAdmin)

## Version

1.0.a

## Features

* Converts the default Django Admin panel into a full fledged dashboard into a clean and professional looking Ela Admin
* Sidebar menu with configurable icons
* Top menu with configurable buttons
* New look for all Django Admin pages
* Branding by adding logos
* [Chart js](https://www.chartjs.org/) based widgets which loads data after page load and completely configurable via http apis

## Screenshots

### Login Page
![Login](https://github.com/eshandas/djello/blob/master/screenshots/login.png?raw=true)

### Dashboard with Configurable Widgets
![Dashboard 1](https://github.com/eshandas/djello/blob/master/screenshots/dashboard_1.png?raw=true)
![Dashboard 2](https://github.com/eshandas/djello/blob/master/screenshots/dashboard_2.png?raw=true)

### Custom Header Links
![Header Links](https://github.com/eshandas/djello/blob/master/screenshots/header_links.png?raw=true)

### Changelist Page
![Changelist](https://github.com/eshandas/djello/blob/master/screenshots/changelist.png?raw=true)
![Changelist Search](https://github.com/eshandas/djello/blob/master/screenshots/changelist_search.png?raw=true)

### Model List Page
![Model List](https://github.com/eshandas/djello/blob/master/screenshots/app_list.png?raw=true)

### Model Update Page
![Model Update](https://github.com/eshandas/djello/blob/master/screenshots/model_list.png?raw=true)

### Logout Page
![Logout](https://github.com/eshandas/djello/blob/master/screenshots/logout.png?raw=true)


## Dependencies

* Django>=2.0
* django-widget-tweaks>=1.4.3

## Installation

Using pip

```
pip install djello
```

## Setup

* Add in app list before 'django.contrib.admin'

```
'djello',
'django.contrib.admin'
...
```

* Add Djello settings in settings.py to configure basic features and dashboard

```
DJELLO = {
    'header_logo': 'djello/images/logo.png',
    'welcome_logo': 'djello/images/logo.png',
    'icons': [],
    'header_links': [('/api/', 'fa-rss'), ('/flower/', 'fa-tasks')],
    'menu': {
        'appauth': {
            'icon': 'fa-users',
            'model_icons': {
                'AppUser': 'fa-user',
                'Role': 'fa-briefcase'}},
        'sample_app': {
            'icon': 'fa-tasks',
            'model_icons': {
                'Post': 'fa-bullhorn'}}},
    'dashboard': [
        [
            {
                'widget': 'stat-widget',
                'id': 'revenue',
                'icon': 'fa-money',
                'color': 'flat-color-1',
                'size': '3',
                'data_url': 'sample_app_api:revenue'
            }, {
                'widget': 'stat-widget',
                'id': 'sales',
                'icon': 'fa-gift',
                'color': 'flat-color-2',
                'size': '3',
                'data_url': 'sample_app_api:sales'
            }, {
                'widget': 'stat-widget',
                'id': 'logsProcessed',
                'icon': 'fa-gears',
                'color': 'flat-color-3',
                'size': '3',
                'data_url': 'sample_app_api:logs_processed'
            }, {
                'widget': 'stat-widget',
                'id': 'peanutsEaten',
                'icon': 'fa-lemon-o',
                'color': 'flat-color-4',
                'size': '3',
                'data_url': 'sample_app_api:peanuts_eaten'
            }
        ],
        [
            {
                'widget': 'graph-widget',
                'id': '',
                'size': '12',
                'data_url': '',
            }
        ],
        [
            {'widget': 'recent-actions-widget', 'id': '', 'size': '6'},
            {'widget': 'chat-widget', 'id': '', 'size': '6'}
        ],
        [
            {
                'widget': 'chartjs-widget',
                'id': 'salesChart',
                'size': '6',
                'data_url': 'sample_app_api:yearly_sales',
            }, {
                'widget': 'chartjs-widget',
                'id': 'barChart',
                'size': '6',
                'data_url': 'sample_app_api:bar_chart',
            }
        ],
        [
            {
                'widget': 'chartjs-widget',
                'id': 'radarChart',
                'size': '6',
                'data_url': 'sample_app_api:radar_chart',
            }, {
                'widget': 'chartjs-widget',
                'id': 'doughnutChart',
                'size': '6',
                'data_url': 'sample_app_api:doughnut_chart',
            }
        ]
    ],
}

```


## Usage

Once Djello is installed and setup is done, it will automatically replace the default admin template with Ela Admin template.

### Widgets

Right now only the below listed widgets are supported by Djello, that too only in the Dashboard page. However, I plan to include the ability to add widgets in other pages as well.

The Dashboard can be configured by adding the **dashboard** key in the Djello settings dict. **dashboard** is a list of list, where each internal list is a row (bootstrap row) in the template. E.g:

```
...
'dashboard': [
    [<row 1 widgets>],
    [<row 2 widgets>],
    ...
]
...
```

Each widget has its own configuration dict as mentioned below:

#### Stat Widget

* Configuration:

```
{
    'widget': 'stat-widget',  # Name
    'id': 'revenue',  # Unique id to be provided
    'icon': 'fa-money',  # Font Awesome icon
    'color': 'flat-color-1',  # Choose color from: flat-color-1, flat-color-2, flat-color-3, flat-color-4, flat-color-5
    'size': '3',  # Bootstrap grid width (12 means the entire width)
    'data_url': 'sample_app_api:revenue'  # Url (API) to fetch data from
}
```

* Data schema:

```
{"mainText":719075,"subText":"Revenue"}
```

#### Recent Actions Widget

Shows Django Admin's recent actions

* Configuration:

```
{'widget': 'recent-actions-widget', 'id': 'recentActions', 'size': '6'}
```

#### Chartjs Widget

Any Chartjs widget can be embedded by providing the chart type, chart display configurations and data from the api.

* Configuration

```
{
    'widget': 'chartjs-widget',
    'id': 'salesChart',
    'size': '6',
    'data_url': 'sample_app_api:yearly_sales',
}
```

* Data schema:

Below is an example which will add a **line graph**. This could be changed to any other graph supported by Graphjs just by changing the graph configurations and the data in your API. Visit [Chartjs website](https://www.chartjs.org/) and explore other kinds of charts.

```
{
  "label": "Yearly Sales",
  "type": "line",
  "data": {
    "labels": ["2012", "2013", "2014", "2015", "2016", "2017", "2018"],
    "type": "line",
    "defaultFontFamily": "Montserrat",
    "datasets": [
      {
        "label": "Foods",
        "data": [0, 30, 15, 110, 50, 63, 120],
        "backgroundColor": "transparent",
        "borderColor": "rgba(220,53,69,0.75)",
        "borderWidth": 3,
        "pointStyle": "circle",
        "pointRadius": 5,
        "pointBorderColor": "transparent",
        "pointBackgroundColor": "rgba(220,53,69,0.75)"
      },
      {
        "label": "Electronics",
        "data": [0, 50, 40, 80, 35, 99, 80],
        "backgroundColor": "transparent",
        "borderColor": "rgba(40,167,69,0.75)",
        "borderWidth": 3,
        "pointStyle": "circle",
        "pointRadius": 5,
        "pointBorderColor": "transparent",
        "pointBackgroundColor": "rgba(40,167,69,0.75)"
      }
    ]
  },
  "options": {
    "responsive": true,
    "tooltips": {
      "mode": "index",
      "titleFontSize": 12,
      "titleFontColor": "#000",
      "bodyFontColor": "#000",
      "backgroundColor": "#fff",
      "titleFontFamily": "Montserrat",
      "bodyFontFamily": "Montserrat",
      "cornerRadius": 3,
      "intersect": false
    },
    "legend": {
      "display": false,
      "labels": {
        "usePointStyle": true,
        "fontFamily": "Montserrat"
      }
    },
    "scales": {
      "xAxes": [
        {
          "display": true,
          "gridLines": {
            "display": false,
            "drawBorder": false
          },
          "scaleLabel": {
            "display": false,
            "labelString": "Month"
          }
        }
      ],
      "yAxes": [
        {
          "display": true,
          "gridLines": {
            "display": false,
            "drawBorder": false
          },
          "scaleLabel": {
            "display": true,
            "labelString": "Value"
          }
        }
      ]
    },
    "title": {
      "display": false,
      "text": "Normal Legend"
    }
  }
}
```

## Future
