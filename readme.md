# drf공부를 위한 레포

### 프로젝트 구조
    - IDBM 사이트를 클론
    - Model : streamplatform > Watchlist(movie,Tvshow) > Review
    - crawling을 활용하여 watchlist사진 및 파일 추가

### 기능
    -stream platform
        Admin외에는 볼 수만 있도록. ADMIN은 CRUD모두 가능
    -Watchlist
        Admin외에는 볼 수만 있도록. ADMIN은 CRUD모두 가능
        필터기능 , 서치기능, 정렬기능
        pagination
    -Review
        CRUD
        한 유저당 watchlist에 대해 하나의 리뷰만 남길 수 있도록

    -Authentication / Permission
        JWT기반의 인증/인가


### 주요 학습 주제
    - genericview
    - signal / receiver
    - Serializer
    - authentication(DRF_AUTH_TOKEN, JWT)   
    - permissions
    - pagination
    - filter(filter,order,search)
    - throttle
    - testcode
    - Swagger / Tracker
    - User