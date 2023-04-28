# Twitter-Data-extraction-from-timeline(Not including RT)
### このスクリプトは、指定したTwitterアカウントの最新200件のツイートを取得し、それらの情報を含むデータをcsvファイルに書き出すためのものです。

#### 具体的には、以下の作業が行われます。
- Twitter APIの認証情報を設定する。
- Twitter APIオブジェクトを生成する。
- 取得するTwitterアカウントのスクリーン名を指定する。
- api.user_timeline関数を使用して、最新の200件のツイートを取得する。
- 取得したツイートは**リツイートを除外して**フルテキストモードで取得される。取得したツイートはリストに追加される。
- 取得したツイートのうち最も古いツイートのIDを保存し、次に古いツイートを取得するために使用する。
- 取得可能なすべてのツイートを取得するためにプロセスを繰り返す。
- 取得したツイートをcsvファイルに保存する。保存される情報は、ツイートのID、作成日時、いいね数、リツイート数、およびテキスト本文である。
- pandasデータフレームを使用して、保存されたツイートの最初の3つを表示する。<br>

#### 実行にはTwitter APIの認証情報が必要です。
##### 取得できるデータについては、APIリファレンスインデックスをご参照ください。
https://developer.twitter.com/en/docs/api-reference-index<br>
※ Python 3.11.1での動作確認済み
*************************************************************************************************************************************************************************
### This script is used to retrieve the 200 most recent tweets for a given Twitter account and generate a csv file containing this information.

#### Specifically, the following tasks are performed.
- Set the authentication information for Twitter API.
- Generate a Twitter API object.
- Specify the screen name of the Twitter account to retrieve.
- Obtain the latest 200 tweets using the api.user_timeline function.
- The acquired tweets are retrieved in full-text mode, excluding retweets. The acquired tweets are added to the list.
- The ID of the oldest tweet retrieved is saved and used to retrieve the next oldest tweet.
- The process is repeated to retrieve all available tweets.
- Save the retrieved tweets in a csv file. The information to be saved is the ID of the tweet, creation date and time, number of likes, number of retweets, and text body.
- Use the pandas data frame to display the first three stored tweets.<br>
### Use the pandas data frame to display the first three saved tweets.
#### Please refer to the API reference index for the data that can be obtained.
https://developer.twitter.com/en/docs/api-reference-index<br>
※ tested the operation with Python 3.11.1
