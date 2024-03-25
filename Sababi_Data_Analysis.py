{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN7Ax3qIQ4xFkmaFUOY8Q9J",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Topexpert647/Sababi-data-analysis/blob/main/Sababi_Data_Analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Bus Company Data Analysis**\n",
        "By Edwin Kirimi Kinuthia\n",
        "This are my answers for the interview questions on Data Analysis from SABABI INSTITUTE"
      ],
      "metadata": {
        "id": "E8G7lJ6UC4x7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "You have recently started working as a Data Analyst for a bus company. The company wants to improve its operations, so you have been asked to analyze some data regarding the bus lines currently operated by the company. The data you will need to analyze is in this excel file: https://shorturl.at/bosK7\n",
        "\n",
        "** Glossary **\n",
        "\n",
        "Routes Table:\n",
        "bus_num - the number of the bus line\n",
        "intercity - does the bus line start in one city and end another (y = yes / n = no)\n",
        "type - the type of bus service (express/ regular)\n",
        "num_stops - the number of stops made by the bus\n",
        "fare - the cost of a single bus ticket (the price does not change depending on where the passenger gets on/off the bus)\n",
        "FOR EXAMPLE: Bus line 63 is a regular bus route with 34 stops and does not cross city lines. The fare of bus line 63 is $3.50.\n",
        "\n",
        "Times Table:\n",
        "time_of_week - is it a weekday (Mon - Fri) or weekend day (Sat - Sun)\n",
        "bus_num - the number of the bus line\n",
        "first_bus - the departure time of the first bus of the day (same in both directions)\n",
        "last_bus - the departure time of the last bus of the day (same in both directions)\n",
        "frequency - the number of times the bus completes its full route each day.\n",
        "FOR EXAMPLE: On Saturdays, bus line 82 operates between 6:30 AM and 11:45 PM. During that period, it completes its route 45 times. Bus line 82 is an express buss with 9 stops and charges a fare of $12.50.\n",
        "\n",
        "Passengers Table:\n",
        "day - the day of the week\n",
        "bus_num - the number of the bus line\n",
        "average_num_passengers - the average number of passengers per route.\n",
        "FOR EXAMPLE: Bus line 8 averages 45 passengers on Wednesdays and 15 passengers on Saturdays. Between the difference in passengers per route as well as the number of routes per day, bus line 8 generates an average of $18,000 in fares every Wednesday but only $1,500 on Saturdays.\n",
        "1. On average, what is the sum total of revenue generated every Tuesday?\n",
        "\n",
        "\n",
        "> Indented blockTo calculate the total revenue for Tuesday, I will use the bus line (bus_num) as the primary key. From the passengers csv table, the average number of passengers (average_num_passengers) each Tuesday for each bus line should be multiplied by the frequency of each bus line (frequency) during weekdays in the times csv table and the fare of each bus line in the routes csv table.\n",
        "\n"
      ],
      "metadata": {
        "id": "v58rhlv7FIY8"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "Y98Jv_yL_AeP",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 141
        },
        "outputId": "8a4b0a40-4cde-4d1c-f8da-253c3d8327f4"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-b719f7e4-9883-42ee-818b-ec154c842a09\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-b719f7e4-9883-42ee-818b-ec154c842a09\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving passengers.csv to passengers.csv\n",
            "Saving routes.csv to routes.csv\n",
            "Saving times.csv to times.csv\n"
          ]
        }
      ],
      "source": [
        "from google.colab import files\n",
        "uploaded = files.upload()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "The files are now uploaded. Using the pandas module, we load the files in Colab environment."
      ],
      "metadata": {
        "id": "3eFoZDTlDHg9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "passengers_df = pd.read_csv('passengers.csv')\n",
        "routes_df = pd.read_csv('routes.csv')\n",
        "times_df = pd.read_csv('times.csv')"
      ],
      "metadata": {
        "id": "nmqMIQCYi87c"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Data cleaning involves removing the $ from the fare column in the routes CSV and converting the fare column to a float value for our calculations."
      ],
      "metadata": {
        "id": "eIe0ChIOEuch"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "routes_df['fare'] = routes_df['fare'].str.replace('$', '').astype(float)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8vizistJjeLH",
        "outputId": "35c1f621-1e7c-4158-81e9-e6f51f06fa8d"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-5-fb28438ba3b4>:1: FutureWarning: The default value of regex will change from True to False in a future version. In addition, single character regular expressions will *not* be treated as literal strings when regex=True.\n",
            "  routes_df['fare'] = routes_df['fare'].str.replace('$', '').astype(float)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "We now Filter for Tuesday in passengers dataframe and for weekdays in the times dataframe."
      ],
      "metadata": {
        "id": "OAoqJBbUFpDE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "tuesday_passengers = passengers_df[passengers_df['day'] == 'Tuesday']\n",
        "weekday_times = times_df[times_df['time_of_week'] == 'weekday']"
      ],
      "metadata": {
        "id": "m-TyILCVjpej"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "With the filtering done, we now merge both tables to create a merged dataframe."
      ],
      "metadata": {
        "id": "LV4mnQbSGBwl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "merged_df = pd.merge(tuesday_passengers, routes_df, on='bus_num')\n",
        "merged_df = pd.merge(merged_df, weekday_times, on='bus_num')"
      ],
      "metadata": {
        "id": "r_MvDW5xj-_q"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculating revenue for each bus line:"
      ],
      "metadata": {
        "id": "-yspA1wAGVOz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "merged_df['revenue'] = merged_df['average_num_passengers'] * merged_df['fare'] * merged_df['frequency']"
      ],
      "metadata": {
        "id": "A9zpyEKRkLJI"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Sum total revenue for Tuesday:"
      ],
      "metadata": {
        "id": "Ux4vVoZCGjYF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "total_tuesday_revenue = merged_df['revenue'].sum()\n",
        "\n",
        "print(f\"Total Revenue generated every Tuesday: ${total_tuesday_revenue:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JM2LLfjgkaMT",
        "outputId": "79ba19e4-510f-41b4-c478-39a47f0a5659"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total Revenue generated every Tuesday: $120403.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Which bus line brings in the lowest average weekly revenue from ticket sales?\n",
        "> Indented blockTo calculate this, using bus line as the primary key, fare in the routes csv table is multiplied by the frequency of both the weekend (Multiply this frequency by 5 since there are weekday days) and the weekday(multiply this by 2 since there are 2 days during weekends) in the times csv table and the sum of the average number of passengers from Monday to Sunday of each bus line; after comparison, the minimum value is the lowest weekly revenue.\n",
        "We begin by importing the data afresh using the pandas module:\n",
        "\n"
      ],
      "metadata": {
        "id": "k4UO2G_ZGpDz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "passengers_df = pd.read_csv('passengers.csv')\n",
        "routes_df = pd.read_csv('routes.csv')\n",
        "times_df = pd.read_csv('times.csv')"
      ],
      "metadata": {
        "id": "mdHL4tmo9qUR"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Cleaning the fare column in the routes dataframe to remove the dollar sign and convert it to float"
      ],
      "metadata": {
        "id": "2lD6TMfJH3Ef"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "routes_df['fare'] = routes_df['fare'].str.replace('$', '').astype(float)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dzjNb1DV-Cb_",
        "outputId": "ceee9d11-f0b9-4105-c872-b591d7d1d505"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-12-fb28438ba3b4>:1: FutureWarning: The default value of regex will change from True to False in a future version. In addition, single character regular expressions will *not* be treated as literal strings when regex=True.\n",
            "  routes_df['fare'] = routes_df['fare'].str.replace('$', '').astype(float)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Aggregating passengers data by bus_num for the total average passengers per week:"
      ],
      "metadata": {
        "id": "lF9nEjVzIGgl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weekly_passengers = passengers_df.groupby('bus_num')['average_num_passengers'].sum().reset_index()\n"
      ],
      "metadata": {
        "id": "i_Ra3WfW-QTF"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Separating times data into weekdays and weekends, then adjusting frequencies:"
      ],
      "metadata": {
        "id": "b3dYx2yDIPo0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "times_df['adjusted_frequency'] = times_df.apply(lambda x: x['frequency'] * 5 if x['time_of_week'] == 'weekday' else x['frequency'] * 2, axis=1)\n",
        "weekly_frequencies = times_df.groupby('bus_num')['adjusted_frequency'].sum().reset_index()\n"
      ],
      "metadata": {
        "id": "TpjE0A7U-im8"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Merging the tables:"
      ],
      "metadata": {
        "id": "qiBgPYtPIf3o"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "merged_df = pd.merge(weekly_passengers, routes_df, on='bus_num')\n",
        "merged_df = pd.merge(merged_df, weekly_frequencies, on='bus_num')"
      ],
      "metadata": {
        "id": "XcanAW9x-qRv"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculating weekly revenue for each bus line:"
      ],
      "metadata": {
        "id": "LfvXk_02JMvV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "merged_df['weekly_revenue'] = merged_df['average_num_passengers'] * merged_df['fare'] * merged_df['adjusted_frequency']\n"
      ],
      "metadata": {
        "id": "m-Su03q2-zor"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Displaying the weekly revenue for all buses. Python is zero indexed so the lowest will begin at zero."
      ],
      "metadata": {
        "id": "rnGBrwJrJXD4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(merged_df[['bus_num', 'weekly_revenue']].sort_values(by='weekly_revenue', ascending=False))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WvYxcoLeAzZm",
        "outputId": "2a36296d-1ca6-4f90-87e1-e2264ba7aad8"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    bus_num  weekly_revenue\n",
            "25       94        713550.0\n",
            "16       51        543720.0\n",
            "24       90        533000.0\n",
            "15       46        496125.0\n",
            "21       82        402187.5\n",
            "4         8        396000.0\n",
            "26       99        362250.0\n",
            "14       42        345950.0\n",
            "12       31        343562.5\n",
            "3         5        322000.0\n",
            "9        19        271250.0\n",
            "20       77        212000.0\n",
            "23       89        188125.0\n",
            "7        17        175200.0\n",
            "18       63        143220.0\n",
            "22       85        114975.0\n",
            "17       58        107065.0\n",
            "13       35         92400.0\n",
            "11       28         92120.0\n",
            "1         2         90965.0\n",
            "6        14         88567.5\n",
            "2         3         87000.0\n",
            "8        18         73150.0\n",
            "10       22         62842.5\n",
            "5        10         54827.5\n",
            "19       68         48440.0\n",
            "0         1         40670.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Finding and displaying the bus line with the lowest average weekly revenue:"
      ],
      "metadata": {
        "id": "Xvo--uiyJsOD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lowest_revenue_bus = merged_df.loc[merged_df['weekly_revenue'].idxmin()]\n",
        "\n",
        "print(f\"Bus line {lowest_revenue_bus['bus_num']} brings in the lowest average weekly revenue from ticket sales: ${lowest_revenue_bus['weekly_revenue']:.2f}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5pESFbMB--Q1",
        "outputId": "772d95bd-a9d5-4caf-bad6-d512afac72f3"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bus line 1 brings in the lowest average weekly revenue from ticket sales: $40670.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. On average, it costs the company $2 per stop on each route. For example, a bus line with 10 stops and has a frequency of 5 routes per day is $100 in daily operational costs. The bus company is considering shutting some lines down over the weekends. Any bus line where the weekend operational costs are more than 50% of the weekend revenue is deemed 'problematic' by the bus company.\n",
        "\n",
        "How many problematic bus lines are there?\n",
        "\n",
        "> Indented blockTo get the Total weekend revenue for each bus (bus line will be the primary key), the average number of passengers each bus line  on Saturday and Sunday summed (from the passengers csv table). Then the result is multiplied by fare in the routes csv table. The result is multiplied by double the frequency (double frequency since there are 2 days during weekend) from times csv table. To the operational cost is then calculated by multiplying 2 by the number of stops (num_stops) and double the frequency (for the two days in the weekend) in the routes csv table for comparison.\n",
        "\n"
      ],
      "metadata": {
        "id": "BiSqjrLiNKAJ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Loading the datasets afresh:\n",
        "\n"
      ],
      "metadata": {
        "id": "Dpl4FoPhN6Wh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "passengers_df = pd.read_csv('passengers.csv')\n",
        "routes_df = pd.read_csv('routes.csv')\n",
        "times_df = pd.read_csv('times.csv')"
      ],
      "metadata": {
        "id": "i51ou3RAOX56"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Cleaning the fare column in the routes dataframe:"
      ],
      "metadata": {
        "id": "ifjKbh_oOf_-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "routes_df['fare'] = routes_df['fare'].str.replace('$', '').astype(float)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R6LdA1ZhOmrr",
        "outputId": "2c3a2fcf-23ae-49b1-fe38-5b92fc0fd23f"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-20-fb28438ba3b4>:1: FutureWarning: The default value of regex will change from True to False in a future version. In addition, single character regular expressions will *not* be treated as literal strings when regex=True.\n",
            "  routes_df['fare'] = routes_df['fare'].str.replace('$', '').astype(float)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Aggregating weekend passenger data and sum the average passengers for Saturday and Sunday"
      ],
      "metadata": {
        "id": "TZDlhcLHTBQI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weekend_passengers = passengers_df[passengers_df['day'].isin(['Saturday', 'Sunday'])]\n",
        "weekend_passengers_sum = weekend_passengers.groupby('bus_num')['average_num_passengers'].sum().reset_index()"
      ],
      "metadata": {
        "id": "BCu9gme9TJJS"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Correctly setting weekend frequencies to avoid SettingWithCopyWarning"
      ],
      "metadata": {
        "id": "0rZRxA77TPVN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weekend_times = times_df[times_df['time_of_week'] == 'weekend'].copy()\n",
        "weekend_times.loc[:, 'weekend_frequency'] = weekend_times['frequency'] * 2\n",
        "weekend_frequencies = weekend_times[['bus_num', 'weekend_frequency']]"
      ],
      "metadata": {
        "id": "15mP4gOMTXqv"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculating weekend revenue (average passengers * fare * doubled frequency)"
      ],
      "metadata": {
        "id": "lEAEtWHQThYM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weekend_revenue = pd.merge(weekend_passengers_sum, routes_df, on='bus_num')\n",
        "weekend_revenue = pd.merge(weekend_revenue, weekend_frequencies, on='bus_num')\n",
        "weekend_revenue['total_weekend_revenue'] = weekend_revenue['average_num_passengers'] * weekend_revenue['fare'] * weekend_revenue['weekend_frequency']"
      ],
      "metadata": {
        "id": "N-EILMc6Tl3m"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Calculating the operational costs (2 * num_stops * doubled frequency for the weekend)"
      ],
      "metadata": {
        "id": "Bn95nJh9Tw0O"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weekend_revenue['operational_cost'] = 2 * weekend_revenue['num_stops'] * weekend_revenue['weekend_frequency']"
      ],
      "metadata": {
        "id": "WYkOwOY4T2If"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Identifying problematic bus lines (where operational costs > 50% of weekend revenue)"
      ],
      "metadata": {
        "id": "oLqT-jtSUOcU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "weekend_revenue['is_problematic'] = weekend_revenue['operational_cost'] > (weekend_revenue['total_weekend_revenue'] * 0.5)"
      ],
      "metadata": {
        "id": "lRJSbHCeUWGD"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        " Preparing and displaying the final list with all bus lines, their weekend revenue, and operational costs:"
      ],
      "metadata": {
        "id": "yqspj_J8Vv7V"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "final_list = weekend_revenue[['bus_num', 'total_weekend_revenue', 'operational_cost']].sort_values(by='bus_num')\n",
        "\n",
        "final_list"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 896
        },
        "id": "Cw2UPo54VnLD",
        "outputId": "f4ea0ea1-7078-47f0-e398-d70d165b63a4"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    bus_num  total_weekend_revenue  operational_cost\n",
              "0         1                 2660.0               680\n",
              "1         2                 9310.0              2584\n",
              "2         3                12450.0               600\n",
              "3         5                22500.0              1200\n",
              "4         8                 6600.0              1800\n",
              "5        10                 5775.0              1380\n",
              "6        14                 6090.0              2040\n",
              "7        17                15000.0               960\n",
              "8        18                10290.0              3360\n",
              "9        19                12300.0              1800\n",
              "10       22                 9800.0              3000\n",
              "11       28                 8680.0              1680\n",
              "12       31                17000.0               440\n",
              "13       35                 4060.0              1160\n",
              "14       42                26400.0              4440\n",
              "15       46                31500.0              1440\n",
              "16       51                44840.0              3952\n",
              "17       58                10640.0              3360\n",
              "18       63                19110.0              4760\n",
              "19       68                 4095.0              2100\n",
              "20       77                23625.0               900\n",
              "21       82                51750.0              1620\n",
              "22       85                 7000.0              1900\n",
              "23       89                15000.0               800\n",
              "24       90                52000.0              1600\n",
              "25       94                47200.0              3840\n",
              "26       99                24120.0              2304"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-86332002-18f5-4e1b-bf1b-ad601db983c8\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>bus_num</th>\n",
              "      <th>total_weekend_revenue</th>\n",
              "      <th>operational_cost</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2660.0</td>\n",
              "      <td>680</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>9310.0</td>\n",
              "      <td>2584</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>12450.0</td>\n",
              "      <td>600</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5</td>\n",
              "      <td>22500.0</td>\n",
              "      <td>1200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>8</td>\n",
              "      <td>6600.0</td>\n",
              "      <td>1800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>10</td>\n",
              "      <td>5775.0</td>\n",
              "      <td>1380</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>14</td>\n",
              "      <td>6090.0</td>\n",
              "      <td>2040</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>17</td>\n",
              "      <td>15000.0</td>\n",
              "      <td>960</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>18</td>\n",
              "      <td>10290.0</td>\n",
              "      <td>3360</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>19</td>\n",
              "      <td>12300.0</td>\n",
              "      <td>1800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>22</td>\n",
              "      <td>9800.0</td>\n",
              "      <td>3000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>28</td>\n",
              "      <td>8680.0</td>\n",
              "      <td>1680</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>31</td>\n",
              "      <td>17000.0</td>\n",
              "      <td>440</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>35</td>\n",
              "      <td>4060.0</td>\n",
              "      <td>1160</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>42</td>\n",
              "      <td>26400.0</td>\n",
              "      <td>4440</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>46</td>\n",
              "      <td>31500.0</td>\n",
              "      <td>1440</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>51</td>\n",
              "      <td>44840.0</td>\n",
              "      <td>3952</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>58</td>\n",
              "      <td>10640.0</td>\n",
              "      <td>3360</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>63</td>\n",
              "      <td>19110.0</td>\n",
              "      <td>4760</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>68</td>\n",
              "      <td>4095.0</td>\n",
              "      <td>2100</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>77</td>\n",
              "      <td>23625.0</td>\n",
              "      <td>900</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>82</td>\n",
              "      <td>51750.0</td>\n",
              "      <td>1620</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>85</td>\n",
              "      <td>7000.0</td>\n",
              "      <td>1900</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>89</td>\n",
              "      <td>15000.0</td>\n",
              "      <td>800</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>90</td>\n",
              "      <td>52000.0</td>\n",
              "      <td>1600</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>94</td>\n",
              "      <td>47200.0</td>\n",
              "      <td>3840</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>99</td>\n",
              "      <td>24120.0</td>\n",
              "      <td>2304</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-86332002-18f5-4e1b-bf1b-ad601db983c8')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-86332002-18f5-4e1b-bf1b-ad601db983c8 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-86332002-18f5-4e1b-bf1b-ad601db983c8');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-82b154ff-11f3-4053-a09e-9062f59c2209\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-82b154ff-11f3-4053-a09e-9062f59c2209')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-82b154ff-11f3-4053-a09e-9062f59c2209 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_ebfc0394-f948-4192-bb6a-b4192b0e9565\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('final_list')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_ebfc0394-f948-4192-bb6a-b4192b0e9565 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('final_list');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "final_list",
              "summary": "{\n  \"name\": \"final_list\",\n  \"rows\": 27,\n  \"fields\": [\n    {\n      \"column\": \"bus_num\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 32,\n        \"min\": 1,\n        \"max\": 99,\n        \"num_unique_values\": 27,\n        \"samples\": [\n          18,\n          35,\n          19\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"total_weekend_revenue\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 14929.576545919037,\n        \"min\": 2660.0,\n        \"max\": 52000.0,\n        \"num_unique_values\": 26,\n        \"samples\": [\n          10290.0,\n          44840.0,\n          2660.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"operational_cost\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 1212,\n        \"min\": 440,\n        \"max\": 4760,\n        \"num_unique_values\": 25,\n        \"samples\": [\n          3360,\n          4760,\n          680\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Counting problematic bus lines:\n",
        "\n"
      ],
      "metadata": {
        "id": "Cxk9BCCvUd_x"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "problematic_lines_count = weekend_revenue['is_problematic'].sum()"
      ],
      "metadata": {
        "id": "mYIC4z30UjC9"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Displaying problematic bus lines and the count:"
      ],
      "metadata": {
        "id": "Msx4Mt5uUrJD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "problematic_lines = weekend_revenue[weekend_revenue['is_problematic']]\n",
        "\n",
        "print(f\"Number of problematic bus lines: {problematic_lines_count}\")\n",
        "problematic_lines[['bus_num', 'total_weekend_revenue', 'operational_cost']]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 98
        },
        "id": "HY3KROUBUuOY",
        "outputId": "23fdc565-9b48-4505-8dbc-2c29620daa16"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Number of problematic bus lines: 1\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    bus_num  total_weekend_revenue  operational_cost\n",
              "19       68                 4095.0              2100"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-db086a10-043e-4180-b1e4-02655b3b3c1c\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>bus_num</th>\n",
              "      <th>total_weekend_revenue</th>\n",
              "      <th>operational_cost</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>68</td>\n",
              "      <td>4095.0</td>\n",
              "      <td>2100</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-db086a10-043e-4180-b1e4-02655b3b3c1c')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-db086a10-043e-4180-b1e4-02655b3b3c1c button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-db086a10-043e-4180-b1e4-02655b3b3c1c');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "summary": "{\n  \"name\": \"problematic_lines[['bus_num', 'total_weekend_revenue', 'operational_cost']]\",\n  \"rows\": 1,\n  \"fields\": [\n    {\n      \"column\": \"bus_num\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": null,\n        \"min\": 68,\n        \"max\": 68,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          68\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"total_weekend_revenue\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": null,\n        \"min\": 4095.0,\n        \"max\": 4095.0,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          4095.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"operational_cost\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": null,\n        \"min\": 2100,\n        \"max\": 2100,\n        \"num_unique_values\": 1,\n        \"samples\": [\n          2100\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    }
  ]
}