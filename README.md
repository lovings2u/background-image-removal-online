## rorodata 사용법 및  image-removal(코드 수정)

*본 자료는 rorodata tutorial과 image-removel 가이드를 참고했으며, 온라인에 있는 이미지만 변경할 수 있게 코드가 수정됐습니다.*



### roro setting

[참고자료](https://rorodata.com/docs/tutorials/image-style-transfer/)

- 진행하기 이전에 rorodata에 가입이 완료되어 있어야 합니다.

```shell
$ pip3 install roro
$ git clone https://github.com/rorodata/style-transfer-demo.git
$ cd style-transfer-demo
$ roro login
$ roro create <App Name>
```

*roro.yml*

```yml
project: <App-Name> 
runtime: python3-keras

services:
  - name: default
    function: <file name>.<function name>
    cors_allow_origins: "*"
```

- `<App-Name>` : create시 작성한 app name
- `<file name>`: API 형태로 동작시킬 파일의 이름
- `<function name>` : 동작하는 파일 내에서 동작시킬 함수



```shell
$ roro deploy
```

- 코드 수정시 해당 명령어만 실행하면 적용됨



```shell
$ sudo apt-get update
$ sudo apt-get install imagemagick
```



*test.rb*

```ruby
system "python3 test.py <file url>"
system "convert -fill none -fuzz 5% -draw 'matte 0,0 floodfill' output.png real_output.png"
```

- `<file url>` : 배경제거 하고자 하는 이미지 url
- 기본적으로 이미지의 배경이 삭제되는 것이 아니라 검정색으로 처리되어 나오기 때문에 imagemagick로 다시한번 처리해줌



*학습되는 모델이 인물'사진'인 것 같다는 느낌이 많이 듬. 이모티콘 제작을 위해서는 해당 모델에 대한 학습이 다시 필요할 것 같음.*

