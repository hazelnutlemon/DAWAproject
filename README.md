# DAWAproject
졸업작품 프로젝트 2019.12~2020.11

프로젝트 개요
웹소설의 인기와 트렌드에 따른 작품 양산화로 인하여,  작품의 질이 독자가 원하는 바에 미치지 못하고 있다. 독자 또한 이를 SNS나 커뮤니티 등에서 직접 그 의견을 내비치고 있다.
또한, 플랫폼 내에서도 독자는 리뷰를 남기는데 사이트에 따라 독자의 나이나 성별등의 차이가 있어 리뷰의 방식도 저마다 다른 특징을 가진다.
따라서, 이러한 SNS, 커뮤니티, 플랫폼 내 댓글을 각 특징을 살려서, 적절한 분석을 거쳐 그 결과를 보이면 작가, 독자, 기업측면에서 서로에게 도움이 되는 Data가 될 수 있을 것이며,
특히, 독자에게 작품 판별에 대한 추가적인 지표를 제공하기 위함이다.

---------------------------------------------------------------------
작품에 대한 정보와 분석에 필요한 Data를 추출하기 위해 선택한 사이트는 다음과 같다.
---------------------------------------------------------------------
플랫폼
Kakaopage, Munpia, Joara, Naver_Series, Ridibooks

SNS : Instagram, Twitter

Community : Dcinside, Instiz

Blog : Daum, Naver,Tistory

---------------------------------------------------------------------
각 사이트에 대한 크롤링 정보는 다음과 같다.
---------------------------------------------------------------------
Platform :
제목, 장르, 저자, 완결여부, 이미지(표지), 연령제한, 연재화수, 출간일, 출판사, 작품소개, 플랫폼별 링크
(Ridibooks, Joara, Naver_Series는 platform에서 제공하는 댓글 크롤링 추가)

SNS : 작성 내용, 작성 날짜

Community : 제목, 작성 날짜, 작성내용, 댓글

Blog : 제목, 날짜, 저자(블로그 주인명), 작성내용


---------------------------------------------------------------------
크롤링된 Data는 Data마다 서로다른 특징을 갖고 있기때문에 의미있는 Data 분석을 위해 3가지 분석을 시행한다.
---------------------------------------------------------------------
1. TextRanK
SNS나 커뮤니티의 경우 실시간 의사소통이 이루어지는 공간이므로, 작품에 대한 '최신 이슈'를 파악하기 용이하다고 판단한다.
따라서, TextRank 분석을 통하여 독자들에게 작품 관련으로 어떠한 이슈가 있는지 보여주고자 한다.

2. Sentimental Analysis
댓글의 경우, 일반적인 리뷰보다 Data가 많고 각 댓글의 양이 길지 않기때문에 각 기간별로 긍부정도를 판단하여,
작품의 긍부정 추이를 독자에게 제공할 수 있으리라 판단한다.
또한, 그 추이는 작가에게도 독자들에게 어떠한 반응이 있는지 보다 쉽게 판단내릴 수 있게 도울 수 있다.

3. Aspect Mining
Blog 같은 경우에는, SNS, 커뮤니티, 플랫폼의 댓글보다 훨씬 길고 자세한 리뷰를 담고 있고,
글의 저자 스스로 해당 작품속의 주인공, 스토리, 분위기 등의 종합적인 판단을 내리고 있기 때문에
이를 종합하여 작품 속 주인공, 스토리, 분위기 등과 연관성이 높은 형용사를 추출하여
작품을 판단할 수 있는 지표를 생성하고자 한다.

---------------------------------------------------------------------
각 크롤러 및 분석 도구에 필요한 모듈과 Input과 Output 그리고 활용 경과는 다음과 같다.
---------------------------------------------------------------------
Crawler
---------------------------------------------------------------------
  1. Flatform
  
    1) Ridibooks
    
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
      
    2) Kakaopage
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
    3) Naver_Series
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
    4) Munpia
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
    5) Joara
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
  2. SNS(Crawler)
  
    1) Instagram
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
    2)Twitter
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
  3. Community(Crawler)
  
    1) Dcinside
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
    2) Instiz
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
  4. Blog(Crawler)
  
    1) Daum
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
    2) Tistory
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
    3) Naver
      
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
Analysis Tool
---------------------------------------------------------------------

  1) TextRank
    
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
  2) Sentimental Analysis
    
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
  3) Aspect Mining
    
      Required Module
      ---------------------------------------------------------------------
      
      Input Argument
      ---------------------------------------------------------------------
      
      Output Argument
      ---------------------------------------------------------------------
      
      Example of Result
      ---------------------------------------------------------------------
      
---------------------------------------------------------------------
각 크롤러 및 분석 도구의 성능 향상 혹은 기능 향상을 위해서는 다음과 같은 내용이 가능하다.
---------------------------------------------------------------------

Crawler
---------------------------------------------------------------------

  1) Kakaopage같은 경우, PC에서 댓글을 확인할 수 있는 기능이 신설되어 Sentimental Analysis에 활용이 가능하다.
  
Analysis Tool
---------------------------------------------------------------------

  1) TextRank 외에 최근에 나온 Upgrade version의 TextRankR 모듈 등을 활용한다면, 좀 더 좋은 결과를 도출할 수 있을 것이다.
  
  2) Keras가 아닌 Kobert와 같이 '한국어'에 특화된 분석 module을 활용한다면, 분석의 정확도를 상승시킬 수 있다.
  
  3) Aspect Mining에서, '1) 항목'에서 언급한 Lexarankr등의 모듈을 활용한다면,
      각 Blog의 결과를 종합하여 핵심적인 문장을 추출해낼 수 있는데, 그것 또한 좋은 Data일 것이다.
