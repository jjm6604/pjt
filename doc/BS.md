# banksnap

## 프로젝트 구조
src
 ┣ assets
 ┃ ┣ brand
 ┃ ┃ ┣ bootstrap-logo-white.svg
 ┃ ┃ ┗ bootstrap-logo.svg
 ┃ ┣ css
 ┃ ┃ ┣ bootstrap.css
 ┃ ┃ ┣ bootstrap.css.map
 ┃ ┃ ┣ bootstrap.min.css
 ┃ ┃ ┣ bootstrap.min.css.map
 ┃ ┃ ┣ bootstrap.rtl.min.css
 ┃ ┃ ┣ bootstrap.rtl.min.css.map
 ┃ ┃ ┣ cover.css
 ┃ ┃ ┣ modals.css
 ┃ ┃ ┗ signin.css
 ┃ ┣ dist
 ┃ ┃ ┣ css
 ┃ ┃ ┃ ┣ bootstrap.min.css
 ┃ ┃ ┃ ┣ bootstrap.min.css.map
 ┃ ┃ ┃ ┣ bootstrap.rtl.min.css
 ┃ ┃ ┃ ┗ bootstrap.rtl.min.css.map
 ┃ ┃ ┗ js
 ┃ ┃ ┃ ┣ bootstrap.bundle.min.js
 ┃ ┃ ┃ ┗ bootstrap.bundle.min.js.map
 ┃ ┣ js
 ┃ ┃ ┣ bootstrap.bundle.min.js
 ┃ ┃ ┣ bootstrap.bundle.min.js.map
 ┃ ┃ ┗ color-modes.js
 ┃ ┣ coffee.jpg
 ┃ ┣ deposit.jpg
 ┃ ┣ deposit_2.jpg
 ┃ ┣ exlogo.gif
 ┃ ┣ exlogo_1.gif
 ┃ ┣ gold.jpg
 ┃ ┣ local.json
 ┃ ┣ logo_nonbackgroound.png
 ┃ ┣ logo_nonbackgroound_x.png
 ┃ ┣ money.png
 ┃ ┣ stock.jpg
 ┃ ┗ subin_video.mp4
 ┣ components
 ┃ ┣ ArticleList.vue
 ┃ ┣ ArticleListItem.vue
 ┃ ┣ ArticleWrite.vue
 ┃ ┣ CommentList.vue
 ┃ ┣ CommentListItem.vue
 ┃ ┣ CommentWrite.vue
 ┃ ┣ DepositDetailItem.vue
 ┃ ┣ DepositList.vue
 ┃ ┣ DepositListItem.vue
 ┃ ┣ DepositOptionItem.vue
 ┃ ┣ EconomyNewsVideo.vue
 ┃ ┣ MainNavbar.vue
 ┃ ┣ MainSurvey.vue
 ┃ ┣ MainSurveyAnswer.vue
 ┃ ┣ Price.vue
 ┃ ┣ PriceItem.vue
 ┃ ┣ ProfileArticle.vue
 ┃ ┣ ProfileComment.vue
 ┃ ┣ ProfileProduct.vue
 ┃ ┣ Propensity.vue
 ┃ ┗ PropensityWrite.vue
 ┣ router
 ┃ ┗ index.js
 ┣ stores
 ┃ ┗ index.js
 ┣ views
 ┃ ┣ ArticleDetailView.vue
 ┃ ┣ CommunityView.vue
 ┃ ┣ CreateArticleView.vue
 ┃ ┣ DepositView.vue
 ┃ ┣ EconomyNewsView.vue
 ┃ ┣ ExchangeCalculatorView.vue
 ┃ ┣ LoginView.vue
 ┃ ┣ MainView.vue
 ┃ ┣ MapView.vue
 ┃ ┣ PriceView.vue
 ┃ ┣ ProductDetailView.vue
 ┃ ┣ ProfileView.vue
 ┃ ┣ PropensityUpdateView.vue
 ┃ ┣ PropensityView.vue
 ┃ ┣ SavingBankView.vue
 ┃ ┣ SavingView.vue
 ┃ ┗ SignupView.vue
 ┣ App.vue
 ┗ main.js


## 코드

### main.js
```
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'
import 'bootstrap'
// import 'bootstrap/dist/css/bootstrap.min.css'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

app.use(pinia)
app.use(router)

app.mount('#app')
```

### App.vue
```
<script setup>
import MainNavbar from '@/components/MainNavbar.vue';
</script>

<template>
  <MainNavbar />
  <main class="center">
    <router-view />
  </main>
</template>

<style>
@import '@/assets/css/bootstrap.min.css';
/* Bootstrap styles */
body {
  font-family: 'Noto Sans KR', sans-serif;
  /* font-family: 'Nanum Gothic', sans-serif; */
}


.center {
    box-sizing: border-box;
    max-width: 1280px;
    margin: 0 auto;
  }
  @media screen {
  .container {
    max-width: 1280px;
    margin: 0 auto;
  }
}
</style>
```

### router
```src\router\index.js
import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/survey',
      name: 'Survey',
      component: () => import('../components/MainSurvey.vue')
    },
    {
      path: '/survey-answer',
      name: 'SurveyAnswer',
      component: () => import('../components/MainSurveyAnswer.vue')
    },
    {
      path: '/deposit',
      name: 'DepositView',
      component: () => import('../views/DepositView.vue')
    },
    {
      path: '/saving',
      name: 'SavingView',
      component: () => import('../views/SavingView.vue')
    },
    {
      path: '/savingBank',
      name: 'SavingBankView',
      component: () => import('../views/SavingBankView.vue')
    },
    {
      path: '/product/:id',
      name: 'ProductDetailView',
      component: () => import('../views/ProductDetailView.vue')
    },
    {
      path: '/economynews',
      name: 'EconomyNews',
      component: () => import('../views/EconomyNewsView.vue')
    },
    {
      path: '/economynewsvideo',
      name: 'EconomyNewsVideo',
      component: () => import('../components/EconomyNewsVideo.vue')
    },
    {
      path: '/exchange',
      name: 'ExchangeCalculator',
      component: () => import('../views/ExchangeCalculatorView.vue')
    },
    {
      path: '/community',
      name: 'community',
      component: () => import('../views/CommunityView.vue')
    },
    {
      path: '/map/:bank',
      name: 'map',
      component: () => import('../views/MapView.vue')
    },
    {
      path: '/create/article',
      name: 'CreateArticleView',
      component: () => import('../views/CreateArticleView.vue')
    },
    {
      path: '/article/:id',
      name: 'DetailView',
      component: () => import('@/views/ArticleDetailView.vue')
    },
    {
      path: '/login',
      name: 'LoginView',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/signUp',
      name: 'SignUpView',
      component: () => import('@/views/SignUpView.vue')
    },
    {
      path: '/profile/:id',
      name: 'ProfileView',
      component: () => import('@/views/ProfileView.vue')
    },
    {
      path: '/propensity',
      name: 'PropensityView',
      component: () => import('@/views/PropensityView.vue')
    },
    {
      path: '/propensity/update',
      name: 'PropensityUpdateView',
      component: () => import('@/views/PropensityUpdateView.vue')
    },
    {
      path: '/price',
      name: 'PriceView',
      component: () => import('@/views/PriceView.vue')
    },
    
  ]
})

export default router
```

### stores
```src\stores\index.js
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useIndexStore = defineStore('index', () => {
  const router = useRouter()
  const url = ref('http://127.0.0.1:8000')
  const articles = ref([])
  const token = ref(null)
  const user = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getArticles = function () {
    axios({
      method: 'get',
      url: `${url.value}/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        articles.value = res.data
      })
      .catch((err) => {
        articles.value = []
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2, age } = payload
    axios({
      method: 'post',
      url: `${url.value}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
      .then((res) => {
        return login({
          username: username,
          password: password1
        })

      })
      .then((res) => {
        createUserInfo(age)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const createUserInfo = function (age) {
    axios({
      method: 'post',
      url: `${url.value}/user/propensity/`,
      data: {
        age: age,
      },
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const login = function (payload) {
    const { username, password } = payload

    return axios({
      method: 'post',
      url: `${url.value}/accounts/login/`,
      data: {
        username,
        password
      }
    })  
      .then((res) => {
        user.value = username
        token.value = res.data.key
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
        alert('아이디와 비밀번호를 확인해 주세요.')
      })
  }
  const logout = function () {
    axios({
      method: 'post',
      url: `${url.value}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        user.value = null
        router.push({name: 'main'})
      })
      .catch((err) => {
        console.log(err)
      })
  }



  return { url, articles, getArticles, login, signUp, logout, token, isLogin, user }
}, { persist: true })
```

### views
```src\views\ArticleDetailView.vue
a<template>
  <div>
    <h1>
      <RouterLink :to="{ name: 'community' }">📢</RouterLink>
      게시판
    </h1>
    <main class="flex-shrink-0">
    <div v-if="article">
        <div class="container">
          <h1 class="mt-5">제목 : {{ article.title }}</h1>
          <p class="text-end">작성일 : {{ article.created_at }} | 수정일 : {{ article.updated_at }}</p>
          <p class="text-end">작성자 : {{ article.username }}</p>
          <p class="lead">{{ article.content }}</p>
          <div class="text-end ">

            <div v-if="article.username === store.user" class="btn-group" role="group">
              <button @click="deleteArticle" class="btn btn-outline-secondary">삭제</button>
              <RouterLink class="btn btn-outline-secondary"
              :to="{name: 'CreateArticleView', query: { type: 'modify', id: $route.params.id }}">
              수정
              </RouterLink>
            </div>
          </div>
            <hr>
          </div>
        </div>
        <div class="container">

          <CommentList :article-id="$route.params.id" />
          <CommentWrite :article-id="$route.params.id"/>
        </div>
      </main>
      </div>
    </template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useIndexStore } from '@/stores/index'
import { useRoute, useRouter, RouterLink } from 'vue-router'
import CommentList from '@/components/CommentList.vue'
import CommentWrite from '@/components/CommentWrite.vue'
import moment from 'moment'


const store = useIndexStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const createdAt = ref(null)
onMounted(() => {
  axios({
    method: 'get',
    url: `${store.url}/articles/${route.params.id}/`
  })
    .then((res) => {
      article.value = res.data
      article.value.created_at = moment(res.data.created_at).format('YYYY-MM-DD HH:mm:ss')
      article.value.updated_at = moment(res.data.updated_at).format('YYYY-MM-DD HH:mm:ss')
    })
    .catch((err) => {
      console.log(err)
    })
})

const deleteArticle = function() {
  axios({
    method: 'delete',
    url: `${store.url}/articles/${article.value.id}/`,
    // headers: {

    // }
  })
    .then((res) => {
      router.push({ name: 'community' })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style>

</style>
```




```src\views\CommunityView.vue

<template>

    <div class="p-5">
        <h1>커뮤니티</h1>
        
        <ArticleList />
        <div class="text-end" v-if="isLogin">
            <RouterLink class="btn btn-outline-secondary px-4 m-1" :to="{ name: 'CreateArticleView', query:{ type: 'create' }}">글 쓰기</RouterLink>
        </div>
    </div>
    

</template>

<script setup>
import { onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useIndexStore()
const isLogin = store.isLogin
onMounted(() => {
    store.getArticles()
})

</script>

<style scoped>

</style>
```



```src\views\CreateArticleView.vue
<template>
  <div>
    <ArticleWrite
      :type="type"
      :id="articleId"
      />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'
import { useRouter, useRoute } from 'vue-router'
import ArticleWrite from '@/components/ArticleWrite.vue'

const route = useRoute()
const type = ref(route.query.type)
const articleId = ref(route.query.id)
</script>

<style scoped>

</style>
```



```src\views\DepositView.vue

<template>
    <div class="p-5">
        <h1>저축성 상품</h1>
        <ul class="nav nav-tabs">
            <li class="nav-item">

                <RouterLink :to="{ name: 'DepositView' }" class="nav-link active" aria-current="page" >예금</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{ name: 'SavingView' }" class="nav-link">적금</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{ name: 'SavingBankView' }" class="nav-link">저축은행</RouterLink>
            </li>
        </ul>
        <!-- 예금 -->
        <DepositList type="deposit" />        
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import DepositList from "@/components/DepositList.vue"


</script>
<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>
```




```src\views\EconomyNewsView.vue
<template>
<div>
  
  <div class="card p-5 m-5">
    <h3>오늘의 경제 이슈</h3>
    <div class="card-body">
      <ul>
        <div v-for="news in newsList" :key="news.title">
          <a :href="news.link">
            <li v-html="news.title"></li>
          </a>
        </div>
      </ul>
    </div>
  </div>
  <EconomyNewsVideo />
</div>  
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios'
import EconomyNewsVideo from '@/components/EconomyNewsVideo.vue'

const router = useRouter()
const newsList = ref([])
const clientId = import.meta.env.VITE_clientId
const clientSecret = import.meta.env.VITE_clientSecret
const searchQuery = '경제' //'%EA%B8%88%EC%9C%B5'
const displayCount = 10
const startPage = 1
const sortOption = 'sim'
const searchURL = `/v1/search/news?query=${searchQuery}&display=${displayCount}&start=${startPage}&sort=${sortOption}`

onMounted(() => {
  axios.get(searchURL, {
    headers: {
      'X-Naver-Client-Id':clientId,
      'X-Naver-Client-Secret':clientSecret
    }
  })
    .then((response) => {
      newsList.value = response.data.items
    })
    .catch((error) => {
      console.error(error)
    })
})

    // 삼항연산자는 가독성을 위함 / 없어도 boolean값 반환
const imgIsEmpty = computed(() => {
    return newsList.value.length > 0 ? true : false
})
</script>

<style scoped>

a{
  text-decoration: none;
  color: rgb(0, 0, 0);
  line-height: 2;
}
a:hover {
  color: rgb(75, 75, 75);
  font-size: 17px
}
</style>
```




```src\views\ExchangeCalculatorView.vue
<template>
    <div class="p-3">
      <h1>외환상품</h1>
      <br>
      <div>
        <h3>환율 계산하기</h3>
        <div class="rounded-pill bg-light input-container p-3">
          <div class="container p-3">
            <div class="row d-flex align-items-center">
              <div class="col-2">

                보유화폐 : 
              </div>
              <div class="col-5 p-0">

                <select v-model="selectedCur1" class="form-control">
                  <option v-for="data in dataList" :value="data.cur_nm"> {{ data.cur_nm }}</option>            
                </select>
              </div>
              <div class="col-5 p-0">

                <input class="form-control" type="number" v-model="exchangeMoney1">
              </div>
            </div>
          </div>
          ▶️
          <div class="container">
            <div class="row d-flex align-items-center">
              <div class="col-2">
                기준화폐 :
              </div>
              <div class="col-5 p-0">
                <select v-model="selectedCur2" class="form-control">
                  <option v-for="data in dataList" :value="data.cur_nm">{{ data.cur_nm }}</option>            
                </select>
              </div>
              <div class="col-5 p-0">
                <input class="form-control" type="number" v-model="exchangeMoney2" readonly>
              </div>
            </div>
          </div>
        </div>
      </div>
      <br>
      <div>

      <h3>환율 표</h3>
      <table class="table table-hover">
        <thead>
          <tr class="table-info">
            <th scope="col">국가</th>
            <th scope="col">송금 받을 때</th>
            <th scope="col">송금 보낼 때</th>
            <th scope="col">매매 기준율</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="data in dataList">
            <td>{{ data.cur_nm }}</td>
            <td>{{ data.ttb }}</td>
            <td>{{ data.tts }}</td>
            <td>{{ data.deal_bas_r }}</td>
          </tr>
        </tbody>
      </table>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { ref, onMounted, watch } from 'vue'
  import { useIndexStore } from '@/stores/index'
  
  
  const selectedCur1 = ref('미국 달러')
  const selectedCur2 = ref('한국 원')
  
  const exchangeMoney1 = ref(0)
  const exchangeMoney2 = ref(0)
  
  
  const dataList = ref([])
  const store = useIndexStore()
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.url}/bank/exchange/`
    })
      .then((res) => {
        dataList.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  })
  const cur1 = ref(null)
  const cur2 = ref(null)
  
  const exchange = function() {
    cur1.value = dataList.value.find(data => data.cur_nm === selectedCur1.value)
    cur2.value = dataList.value.find(data => data.cur_nm === selectedCur2.value)
    let deal = Number(cur1.value.deal_bas_r.replace(/,/g, '')) / Number(cur2.value.deal_bas_r.replace(/,/g, ''))
    if ((cur1.value.cur_nm === '일본 옌' || cur1.value.cur_nm === '인도네시아 루피아') && (cur2.value.cur_nm !== '일본 옌' || cur2.value.cur_nm !== '인도네시아 루피아')){
      deal /= 100
    }
    if ((cur2.value.cur_nm === '일본 옌' || cur2.value.cur_nm === '인도네시아 루피아') && (cur2.value.cur_nm !== '일본 옌' || cur2.value.cur_nm !== '인도네시아 루피아')){
      deal *= 100
    }

    exchangeMoney2.value = (Number(exchangeMoney1.value) * deal).toFixed(2)
  }
  
  
  
  watch([exchangeMoney1, selectedCur1, selectedCur2], () => {
      exchange()
  })
  
  </script>
  
  <style scoped>
  tr, th, td {
    border-bottom: 1px solid black;
    padding: 3px;
  }

  .input-container {
  display: flex;
  gap: 10px; /* 좌우 간격을 조절할 값 (원하는 간격으로 조절) */
  justify-content: space-around; /* 입력 요소들을 동일한 간격으로 배치 */
  align-items: center; /* 세로 중앙 정렬을 위한 설정 */
}
  </style>
```




```src\views\LoginView.vue
<template>
  <div class="text-center">
    <main class="form-signin">
      <form @submit.prevent="login">
        <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
        <h1 class="h3 mb-3 fw-normal">로그인페이지</h1>
        <div class="form-floating">
          <input type="text" v-model.trim="username" class="form-control" id="floatingInput" placeholder="ID">
          <label for="floatingInput">아이디</label>
        </div>
        <div class="form-floating">
          <input type="password" v-model.trim="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">비밀번호</label>
        </div>
        <button class="w-100 btn btn-lg btn-outline-success" type="submit">로그인</button>
        <p class="mt-5 mb-3 text-muted">안녕하세요, 고객님!</p>
      </form>
    </main>
  </div> 
</template>     
    
<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()
const username = ref('')
const password = ref('')

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  const loginResult = store.login(payload)

  if (!loginResult) {
    // 로그인 실패 시 모달을 표시
    showErrorModal.value = true
  }
}
const closeErrorModal = function () {
  // 모달을 닫을 때 호출
  showErrorModal.value = false
}

</script>

<style scoped>
/* Bootstrap styles */
@import '@/assets/css/bootstrap.min.css';

/* Additional styles */
@import '@/assets/css/signin.css';

.text-center {
  text-align: center;
}
</style>
```




```src\views\MainView.vue
<!-- MainView.vue -->
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const showModal = () => {
  router.push('/survey')
}

</script>

<template>
  <div class="d-flex h-100 text-center text-black bg-light pt-5">
    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">

      <main class="px-3">
        <h1>당신의 자산을 투자하세요.</h1>
        <br>
        <p class="lead">가치있는 자산을 만들어, 고객의 오늘을 즐겁게.</p>
        <p class="lead">당신이 직접 만들어 가는 가치 다양한 상품 확인하고 여러분의 자산을 투자하세요.</p> 
        <p class="lead">Bank Snap이 함께하겠습니다.</p>
        <p class="lead">
          <a href="#" class="btn btn-lg btn-secondary fw-bold border-white bg-gray" @click.prevent="showModal">준비되셨나요?</a>
        </p>
      </main>
      <video autoplay muted loop>
        <source src="../assets/subin_video.mp4" type="video/mp4" />
      </video>
    </div>
  </div>
  
</template>

<style scoped>

</style>
```




```src\views\MapView.vue
<template>
  <div class="container p-5">
    <h1>은행 찾기</h1>
    <!-- <div class="containe"></div> -->
    <div class="row p-3">
        <div class="col-2 p-1">
            <select v-model="selectedLocal1" class="form-control">    
                <option v-for="local1 in localType1" :key="local1" :value="local1">
                    {{ local1 }}
                </option>            
            </select>
        </div>
        <div class="col-2 p-1">

            <select v-model="selectedLocal2" class="form-control">
                <option v-for="local2 in localType2" :key="local2" :value="local2">{{ local2 }}</option>            
            </select>
        </div>
        <div class="col-2 p-1">
            
            <select v-model="selectedLocal3" class="form-control">
                <option v-for="local3 in localType3" :key="local3" :value="local3">{{ local3 }}</option>            
            </select>
        </div>
        <div class="col-2 p-1">
            <select v-model="selecteBank" class="form-control">
                <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
            </select>
        </div>
        <div class="col-2 p-1">
            <button @click="searchPlaces" class="btn btn-secondary col-12">검색하기</button> 
        </div>
        
    </div>
    <br>
    <div class="map_wrap">
    <div id="map" style="width:100%;height:100%;position:relative;overflow:hidden;"></div>
    
    <div id="menu_wrap" class="bg_white">
        <div class="option">
            <div>
              
            </div>
        </div>
        <hr>
        <ul id="placesList"></ul>
        <div id="pagination"></div>
    </div>
</div>
  </div>
</template>



<script setup>
import { ref, onMounted, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import local from "@/assets/local.json"
const API_KEY = import.meta.env.VITE_KAKAO
const map = ref(null);
const infowindow = ref(null); // infowindow 추가
const markers = ref([])
const route = useRoute()
let marker = ''

// select 박스 설정
// const selectLocal1 = ref(Object.keys(local)[0])
// const selectLocal2 = ref(Object.keys(local[selectLocal1.value])[0])
// const selectLocal3 = ref(local[selectLocal1.value][selectLocal2.value][0])
const selectedLocal1 = ref('부산광역시')
const selectedLocal2 = ref('강서구')
const selectedLocal3 = ref('녹산동')
const coords = ref([37.566826, 126.9786567])
const currentLocation = function() {
    

}


const localType1 = ref(Object.keys(local))
const localType2 = computed(() => {
    return Object.keys(local[selectedLocal1.value])
})
const localType3 = computed(() => {
    return local[selectedLocal1.value][selectedLocal2.value]
})

watch(selectedLocal1, () => {
    selectedLocal2.value = Object.keys(local[selectedLocal1.value])[0]
})
watch(selectedLocal2, () => {
    selectedLocal3.value = local[selectedLocal1.value][selectedLocal2.value][0]
})


const banks = ["국민은행","우리은행","신한은행","KEB하나은행","한국스탠다드차타드은행","외한은행","한국시티은행","경남은행","광주은행","대구은행","부산은행","전북은행","제주은행","기업은행","농협","수협","한국산업은행","한국수출입은행"]
const selecteBank = ref(route.params.bank)


onMounted(() => {
    currentLocation()
    if (window.kakao && window.kakao.maps) {
        
        loadMap()
    } else {
        loadScript()
      }
});




// api 스크립트 불러오기
const loadScript = () => {
  const script = document.createElement("script");
  script.src =
    `//dapi.kakao.com/v2/maps/sdk.js?appkey=${API_KEY}&libraries=services&autoload=false`;
  script.onload = () => window.kakao.maps.load(loadMap);
  document.head.appendChild(script);
};

// 맵 출력하기
const loadMap = () => {
    const container = document.getElementById("map");
    navigator.geolocation.getCurrentPosition(
        (res) =>{
            coords.value[0] = res.coords.latitude
            coords.value[1] = res.coords.longitude
            const options = {
                center: new window.kakao.maps.LatLng(coords.value[0], coords.value[1]),
                level: 7,
            };

            map.value = new window.kakao.maps.Map(container, options);
            infowindow.value = new window.kakao.maps.InfoWindow({ zIndex: 1 }); // Correct initialization
            const ps = new kakao.maps.services.Places();
            ps.setMap(map.value)
            // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다\
            const searchOptions = {
                x: coords.value[0],
                y: coords.value[1], 
                radius: 20000,
                useMapCenter: true,
            }
            ps.keywordSearch(selecteBank.value, placesSearchCB, searchOptions);
        }
        ,
        () => {
            alert('위치 정보를 가져오지 못했습니다.')
            const options = {
                center: new window.kakao.maps.LatLng(coords.value[0], coords.value[1]),
                level: 7,
            };

            map.value = new window.kakao.maps.Map(container, options);
            infowindow.value = new window.kakao.maps.InfoWindow({ zIndex: 1 }); // Correct initialization
            searchPlaces();
        }
    )
    
    
  // 키워드로 장소를 검색합니다
  
  
  

};
const searchPlaces = function() {
    const keywordValue = `${selectedLocal1.value} ${selectedLocal2.value} ${selectedLocal3.value} ${selecteBank.value}`
    if (!keywordValue) {
      alert('키워드를 입력해주세요!');
      return;
    }
    const ps = new kakao.maps.services.Places();
    ps.setMap(map.value)
    // 장소검색 객체를 통해 키워드로 장소검색을 요청합니다\
    
    ps.keywordSearch(keywordValue, placesSearchCB);
    
  }
function placesSearchCB(data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {

        // 정상적으로 검색이 완료됐으면
        // 검색 목록과 마커를 표출합니다
        displayPlaces(data);

        // 페이지 번호를 표출합니다
        displayPagination(pagination);

    } else if (status === kakao.maps.services.Status.ZERO_RESULT) {

        alert('검색 결과가 존재하지 않습니다.');
        return;

    } else if (status === kakao.maps.services.Status.ERROR) {

        alert('검색 결과 중 오류가 발생했습니다.');
        return;

    }
}

// 검색 결과 목록과 마커를 표출하는 함수입니다
function displayPlaces(places) {

    let listEl = document.getElementById('placesList'), 
    menuEl = document.getElementById('menu_wrap'),
    fragment = document.createDocumentFragment(), 
    bounds = new kakao.maps.LatLngBounds(), 
    listStr = '';
    
    // 검색 결과 목록에 추가된 항목들을 제거합니다
    removeAllChildNods(listEl);

    // 지도에 표시되고 있는 마커를 제거합니다
    removeMarker();
    
    for ( let i=0; i<places.length; i++ ) {

        // 마커를 생성하고 지도에 표시합니다
        let placePosition = new kakao.maps.LatLng(places[i].y, places[i].x),
        marker = addMarker(placePosition, i, places[i].place_name), 
            itemEl = getListItem(i, places[i]); // 검색 결과 항목 Element를 생성합니다

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        bounds.extend(placePosition);
        // 마커와 검색결과 항목에 mouseover 했을때
        // 해당 장소에 인포윈도우에 장소명을 표시합니다
        // mouseout 했을 때는 인포윈도우를 닫습니다
        (function(marker, title) {
            kakao.maps.event.addListener(marker, 'mouseover', function() {
                displayInfowindow(marker, title);
            });

            kakao.maps.event.addListener(marker, 'mouseout', function() {
                infowindow.value.close();
            });

            itemEl.onmouseover =  function () {
                displayInfowindow(marker, title);
            };

            itemEl.onmouseout =  function () {
                infowindow.value.close();
            };
        })(marker, places[i].place_name);

        fragment.appendChild(itemEl);
    }

    // 검색결과 항목들을 검색결과 목록 Element에 추가합니다
    listEl.appendChild(fragment);
    menuEl.scrollTop = 0;
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    
    map.value.setBounds(bounds);
    
}

// 검색결과 항목을 Element로 반환하는 함수입니다
function getListItem(index, places) {

    let el = document.createElement('li'),
    itemStr = '<span class="markerbg marker_' + (index+1) + '"></span>' +
                '<div class="info">' +
                '   <h5>' + places.place_name + '</h5>';

    if (places.road_address_name) {
        itemStr += '    <span>' + places.road_address_name + '</span>' +
                    '   <span class="jibun gray">' +  places.address_name  + '</span>';
    } else {
        itemStr += '    <span>' +  places.address_name  + '</span>'; 
    }
                
        itemStr += '  <span class="tel">' + places.phone  + '</span>' +
                '</div>';           

    el.innerHTML = itemStr;
    el.className = 'item';

    return el;
}

// 마커를 생성하고 지도 위에 마커를 표시하는 함수입니다
function addMarker(position, idx, title) {
    let imageSrc = 'https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png', // 마커 이미지 url, 스프라이트 이미지를 씁니다
        imageSize = new kakao.maps.Size(36, 37),  // 마커 이미지의 크기
        imgOptions =  {
            spriteSize : new kakao.maps.Size(36, 691), // 스프라이트 이미지의 크기
            spriteOrigin : new kakao.maps.Point(0, (idx*46)+10), // 스프라이트 이미지 중 사용할 영역의 좌상단 좌표
            offset: new kakao.maps.Point(13, 37) // 마커 좌표에 일치시킬 이미지 내에서의 좌표
        },
        markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions),
            marker = new kakao.maps.Marker({
            position: position, // 마커의 위치
            image: markerImage 
        });

    marker.setMap(map.value); // 지도 위에 마커를 표출합니다
    markers.value.push(marker);  // 배열에 생성된 마커를 추가합니다

    return marker;
}

// 지도 위에 표시되고 있는 마커를 모두 제거합니다
function removeMarker() {
    for ( let i = 0; i < markers.value.length; i++ ) {
        markers.value[i].setMap(null);
    }   
    markers.value = [];
}

// 검색결과 목록 하단에 페이지번호를 표시는 함수입니다
function displayPagination(pagination) {
    let paginationEl = document.getElementById('pagination'),
        fragment = document.createDocumentFragment(),
        i; 

    // 기존에 추가된 페이지번호를 삭제합니다
    while (paginationEl.hasChildNodes()) {
        paginationEl.removeChild (paginationEl.lastChild);
    }

    for (i=1; i<=pagination.last; i++) {
        let el = document.createElement('a');
        el.href = "#";
        el.innerHTML = i;

        if (i===pagination.current) {
            el.className = 'on';
        } else {
            el.onclick = (function(i) {
                return function() {
                    pagination.gotoPage(i);
                }
            })(i);
        }

        fragment.appendChild(el);
    }
    paginationEl.appendChild(fragment);
}

// 검색결과 목록 또는 마커를 클릭했을 때 호출되는 함수입니다
// 인포윈도우에 장소명을 표시합니다
function displayInfowindow(marker, title) {
    let content = '<div style="padding:5px;z-index:1;">' + title + '</div>';

    infowindow.value.setContent(content);
    infowindow.value.open(map.value, marker);
}

 // 검색결과 목록의 자식 Element를 제거하는 함수입니다
function removeAllChildNods(el) {   
    while (el.hasChildNodes()) {
        el.removeChild (el.lastChild);
    }
}
</script>

<style scoped>
.map_wrap, .map_wrap * {margin:0;padding:0;font-family:'Malgun Gothic',dotum,'돋움',sans-serif;font-size:12px;}
.map_wrap a, .map_wrap a:hover, .map_wrap a:active{color:#000;text-decoration: none;}
.map_wrap {position:relative;width:100%;height:500px;}
#menu_wrap {position:absolute;top:0;left:0;bottom:0;width:250px;margin:10px 0 30px 10px;padding:5px;overflow-y:auto;background:rgba(255, 255, 255, 0.7);z-index: 1;font-size:12px;border-radius: 10px;}
.bg_white {background:#fff;}
#menu_wrap hr {display: block; height: 1px;border: 0; border-top: 2px solid #5F5F5F;margin:3px 0;}
#menu_wrap .option{text-align: center;}
#menu_wrap .option p {margin:10px 0;}  
#menu_wrap .option button {margin-left:5px;}
#placesList li {list-style: none;}
#placesList .item {position:relative;border-bottom:1px solid #888;overflow: hidden;cursor: pointer;min-height: 65px;}
#placesList .item span {display: block;margin-top:4px;}
#placesList .item h5, #placesList .item .info {text-overflow: ellipsis;overflow: hidden;white-space: nowrap;}
#placesList .item .info{padding:10px 0 10px 55px;}
#placesList .info .gray {color:#8a8a8a;}
#placesList .info .jibun {padding-left:26px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_jibun.png) no-repeat;}
#placesList .info .tel {color:#009900;}
#placesList .item .markerbg {float:left;position:absolute;width:36px; height:37px;margin:10px 0 0 10px;background:url(https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png) no-repeat;}
#placesList .item .marker_1 {background-position: 0 -10px;}
#placesList .item .marker_2 {background-position: 0 -56px;}
#placesList .item .marker_3 {background-position: 0 -102px}
#placesList .item .marker_4 {background-position: 0 -148px;}
#placesList .item .marker_5 {background-position: 0 -194px;}
#placesList .item .marker_6 {background-position: 0 -240px;}
#placesList .item .marker_7 {background-position: 0 -286px;}
#placesList .item .marker_8 {background-position: 0 -332px;}
#placesList .item .marker_9 {background-position: 0 -378px;}
#placesList .item .marker_10 {background-position: 0 -423px;}
#placesList .item .marker_11 {background-position: 0 -470px;}
#placesList .item .marker_12 {background-position: 0 -516px;}
#placesList .item .marker_13 {background-position: 0 -562px;}
#placesList .item .marker_14 {background-position: 0 -608px;}
#placesList .item .marker_15 {background-position: 0 -654px;}
#pagination {margin:10px auto;text-align: center;}
#pagination a {display:inline-block;margin-right:10px;}
#pagination .on {font-weight: bold; cursor: default;color:#777;}
</style>
```




```src\views\PriceView.vue
<template>
  <div class="p-5">
    <h1>현물 상품</h1>
    <Price />
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import Price from '@/components/Price.vue'


</script>

<style scoped>

</style> 
```



```src\views\ProductDetailView.vue
<template>
    <div>
        <div class="p-5">
            <DepositDetailItem />            
        </div>   
    </div>
</template>

<script setup>
import DepositDetailItem from "@/components/DepositDetailItem.vue"


</script>
<style scoped>

</style>
```




```src\views\ProfileView.vue
<template>
  <div class="text-center p-5">
    <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
    <ul class="nav nav-tabs">
        <li class="nav-item">

            <p class="nav-link active" aria-current="page" >프로필</p>
        </li>
        <li class="nav-item">
            <RouterLink :to="{ name: 'PropensityView' }" class="nav-link">내 금융정보</RouterLink>
        </li>
    </ul>
    <h1 class="p-5">{{ username }} 님의 프로필</h1>
      <div class="card-group">
        <div class="card">
          <div class="card-header text-center">
                <h5>작성 게시글</h5>
            </div>
          <template v-if="articles.length > 0">
            <ProfileArticle :articles="articles" />
          </template>
          <template v-else>
            <div class="card-body">
              <p>작성 게시글이 없습니다.</p>
            </div>
          </template>
        </div>
        <div class="card">
          <div class="card-header text-center">
                <h5>작성 댓글</h5>
            </div>
          <template v-if="comments.length > 0">
            <ProfileComment :comments="comments" />
          </template>
          <template v-else>
            <div class="card-body">
              <p>작성 댓글이 없습니다.</p>
            </div>
          </template>
        </div>
        <div class="card">
          <div class="card-header text-center">
                <h5>관심 상품</h5>
            </div>
          <template v-if="products.length > 0">
            <ProfileProduct :products="products" />
          </template>
          <template v-else>
            <div class="card-body">
              <p>관심 상품이 없습니다.</p>
            </div>
          </template>
        </div>
      </div>
    </div>
    
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'

import ProfileArticle from '@/components/ProfileArticle.vue'
import ProfileComment from '@/components/ProfileComment.vue'
import ProfileProduct from '@/components/ProfileProduct.vue'

const store = useIndexStore()
const route = useRoute()

const username = ref('')
const articles = ref([])
const comments = ref([])
const products = ref([])

onMounted(() => {
  axios({
      method: 'get',
      url: `${store.url}/user/profile/${route.params.id}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) =>{
        username.value = res.data.username
        articles.value = res.data.article_set
        comments.value = res.data.comment_set
        products.value = res.data.like_products
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>

<style>
a {
  color: black;
}
.nav-link {
  color: rgb(173, 173, 173);
}
</style>
```




```src\views\PropensityUpdateView.vue
<template>
  <div class="text-center p-3 m-5">
    <PropensityWrite />
  </div>
</template>

<script setup>
import PropensityWrite from '@/components/PropensityWrite.vue'

</script>

<style scoped>

</style>
```




```src\views\PropensityView.vue
<script setup>
import { RouterLink } from 'vue-router'
import { computed } from 'vue'
import { useIndexStore } from '@/stores/index'
import Propensity from "@/components/Propensity.vue"

const store = useIndexStore()
const user = computed(() => {
  return store.user
})

</script>
<template>
  <div class="text-center p-5">
    <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
    <ul class="nav nav-tabs">
      <li class="nav-item">

          <RouterLink :to="{ name: 'ProfileView' , params:{id: user}}" class="nav-link">프로필</RouterLink>
      </li>
      <li class="nav-item">
          <p class="nav-link active" aria-current="page">내 금융정보</p>
      </li>
  </ul>
    <Propensity />
  </div>
</template>



<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>
```




```src\views\SavingBankView.vue

<template>
    <div class="p-5">
        <h1>저축성 상품</h1>
        <!-- 저축은행 -->
        <ul class="nav nav-tabs">
            <li class="nav-item">

                <RouterLink :to="{ name: 'DepositView' }" class="nav-link">예금</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{ name: 'SavingView' }" class="nav-link">적금</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{ name: 'SavingBankView' }" class="nav-link active" aria-current="page">저축은행</RouterLink>
            </li>
        </ul>
        <DepositList type="savingBank" />        
    </div>
</template>

<script setup>
import DepositList from "@/components/DepositList.vue"


</script>
<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>
```




```src\views\SavingView.vue

<template>
    <div class="p-5">
        <h1>저축성 상품</h1>
        <!-- 적금 -->
        <ul class="nav nav-tabs">
            <li class="nav-item">

                <RouterLink :to="{ name: 'DepositView' }" class="nav-link">예금</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{ name: 'SavingView' }" class="nav-link active" aria-current="page">적금</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{ name: 'SavingBankView' }" class="nav-link">저축은행</RouterLink>
            </li>
        </ul>
        <DepositList type="saving" />        
    </div>
</template>

<script setup>
import DepositList from "@/components/DepositList.vue"


</script>
<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>
```




```src\views\SignupView.vue
<template>
  <div class="text-center">
    <main class="form-signin">
      <form @submit.prevent="signUp">
        <img class="mb-4" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57">
        <h1 class="h3 mb-3 fw-normal">회원가입</h1>
        <div class="form-floating pb-2">
          <input type="text" v-model.trim="username" class="form-control" id="floatingInput" placeholder="ID">
          <label for="floatingInput">아이디</label>
        </div>
        <div class="form-floating">
          <input type="password" v-model.trim="password1" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">비밀번호</label>
        </div>
        <div class="form-floating">
          <input type="password" v-model.trim="password2" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">비밀번호확인</label>
        </div>
        <div class="form-floating pb-2">
          <input type="number" v-model.trim="age" class="form-control" id="floatingInput" placeholder="Age">
          <label for="floatingInput">나이</label>
        </div>
        <button class="w-100 btn btn-lg btn-outline-success" type="submit">Sign in</button>
        <p class="mt-5 mb-3 text-muted">뱅크스냅에 오신 것을 환영합니다!</p>
      </form>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/Index'

const store = useIndexStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const age = ref(null)

const signUp = function() {
  if (!username.value){
    alert("아이디를 입력해 주세요.")
  } else if (!password1.value || !password2.value){
    alert("비밀번호를 입력해 주세요.")
  } else if(password1.value !== password2.value){
    alert("비밀번호가 일치하지 않습니다.")
  } else if(!age.value){
    alert("나이를 입력해 주세요.")
  } else{

    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      age: age.value
    }
    store.signUp(payload)
  }
}

</script>

<style scoped>
/* Bootstrap styles */
@import '@/assets/css/bootstrap.min.css';

/* Additional styles */
@import '@/assets/css/signin.css';
</style>
```



### components
```src\components\ArticleList.vue
<template>
  <div>
    <table class="table">
  <thead>
    <tr class="text-center">
      <th scope="col">번호</th>
      <th scope="col">제목</th>
      <th scope="col">작성일자</th>
      <th scope="col">작성자</th>
    </tr>
  </thead>
  <tbody>
    <ArticleListItem 
    v-for="article in store.articles"
    :key="article.id"
    :article="article"
    />
  </tbody>
  </table>
  </div>
</template>

<script setup>
import { useIndexStore } from '@/stores/index'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useIndexStore()

</script>

```




```src\components\ArticleListItem.vue
<template>
  <tr class="text-center">
    <td>{{ article.id }}</td>
    <td class="text-start">
      <RouterLink :to="{ name: 'DetailView', params: { id: article.id }}">
      {{ article.title }} [{{ article.comment_count }}]
      </RouterLink></td>
    <td>{{ createdAt }}</td>
    <td>{{ article.username }}</td>
  </tr>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import moment from 'moment'

const props = defineProps({
  article: Object
})
const createdAt = ref(moment(props.article.created_at).format('YYYY-MM-DD'))
</script>

<style scoped>
a{
  text-decoration: none;
  color: rgb(0, 0, 0);
  line-height: 2;
}
a:hover {
  color: rgb(133, 133, 133);
}
</style>
```




```src\components\ArticleWrite.vue
<template>
  <div class="p-5">
    <h1>게시글 작성</h1>
    <form @submit.prevent="writeArticle">
      
      <div class="input-group">
        <span class="input-group-text">제목</span>
        <input type="text" v-model.trim="title" id="title" class="form-control">
      </div>
      <br>
      <div class="input-group">
        <span class="input-group-text">내용</span>
        <textarea v-model.trim="content" id="content" class="form-control" rows="10" aria-label="내용"></textarea>
      </div>
      <div class="text-end">

        <input class="btn btn-outline-secondary px-4 m-1" type="submit" value="작성">
      </div>
    </form>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'
import { useRoute, useRouter } from 'vue-router'
const props = defineProps({
  type: String,
  id: Number,
})

const store = useIndexStore()
const router = useRouter()
const route = useRoute()
const title = ref(null)
const content = ref(null)
const type = ref(null)

onMounted(() => {
  type.value = props.type
  if (type.value === 'modify'){
    axios({
    method: 'get',
    url: `${store.url}/articles/${props.id}/`
    })
      .then((res) => {
        title.value = res.data.title
        content.value = res.data.content
      })
      .catch((err) => {
        console.log(err)
      })
  }
})


const writeArticle = function() {
  if (type.value === 'modify'){
    updateArticle()
  } else if (type.value === 'create'){
    createArticle()
  }
}

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.url}/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'DetailView', params: { id: res.data.id } })
    })
    .catch((err) => {
      console.log(err)
    })
}

const updateArticle = function () {
  axios({
    method: 'put',
    url: `${store.url}/articles/${props.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({ name: 'DetailView', params: { id: res.data.id } })
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>

</style>
```




```src\components\CommentList.vue
<template>
  <div>
    <h3>댓글</h3>
    <CommentListItem  
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import CommentListItem from '@/components/CommentListItem.vue'
import axios from 'axios'

const comments = ref(null)
const store = useIndexStore()
const props = defineProps({
  articleId: String,
})
onMounted(() => {
  axios({
      method: 'get',
      url: `${store.url}/articles/comments/${props.articleId}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) =>{
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
})

</script>
```



```src\components\CommentListItem.vue
<template>
  <div>
    <p>
      <div class="container">
        <div class="row">
          <div class="col-auto me-auto">
            {{ comment.username }} : {{ comment.content }}
          </div>
          <div class="col-auto">
            <button v-if="comment.username === store.user" @click="deleteComment" class="btn btn-outline-secondary">댓글 삭제</button>
          </div>
        </div>
      </div>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useIndexStore()
const router = useRouter()
const props = defineProps({
  comment: Object,
})

const deleteComment = function() {
  axios({
    method: 'delete',
    url: `${store.url}/articles/comment/delete/${props.comment.id}/`,
    // headers: {

    // }
  })
    .then((res) => {
      console.log(res.data)
      router.go()
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>
```



```src\components\CommentWrite.vue
<template>
  <div>

    <form @submit.prevent="createComment">
      <div class="input-group">
        <span class="input-group-text">댓글</span>
        <textarea class="form-control" aria-label="With textarea" v-model.trim="content"></textarea>
        <input type="submit" value="댓글 작성" class="btn btn-outline-secondary">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'
import { useRouter } from 'vue-router'
import axios from 'axios'


const store = useIndexStore()
const content = ref(null)
const router = useRouter()
const props = defineProps({
  articleId: String,
})

// console.log(`Token ${store.token}`)
const createComment = function () {
  axios({
    method: 'post',
    url: `${store.url}/articles/comments/${props.articleId}/`,
    data: {
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      // router.push({ name: 'DetailView', params: { id: props.articleId }})
      router.go()
    })
    .catch((err) => {
      console.log(err)
    })
}



</script>

<style scoped>

</style>
```





```src\components\DepositDetailItem.vue

<script setup>
import { ref, onBeforeMount } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'


const store = useIndexStore()
const route = useRoute()
const product = ref(null)
const likeButton = ref(null)
const isData = ref(false)
const isLike = ref(false)
onBeforeMount(() => {
    axios({
        method: 'get',
        url: `${store.url}/bank/product/detail/${route.params.id}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) =>{
        product.value = res.data.product
        if (res.data.is_liked){
            isLike.value = true
        }else {
            isLike.value = false
        }
        isData.value = true
    })
    .catch((err) => {
        console.log(err)
    })
})

const likeProduct = function() {
    axios({
        method: 'post',
        url: `${store.url}/bank/product/like/${route.params.id}/`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res) =>{
        if (res.data.is_liked){
            isLike.value = true
        }else{
            isLike.value = false
        }

    })
    .catch((err) => {
        console.log(err)
    })

}

</script>
<template>
    <div v-if="isData">
        <main>
            <h1 class="text-body-emphasis">💰{{ product.fin_prdt_nm }}💰</h1>
            <br>    
            <p class="fs-5 col-md-8">은행 명 : {{ product.kor_co_nm }}</p>
            
            <p class="fs-5 col-md-8">가입 대상 : {{ product.join_member }}</p>
            <p class="fs-5 col-md-8">가입 방법 : {{ product.join_way }}</p>
            <p class="fs-5 col-md-8">상품 정보</p>
            
            <div class="fs-6 col-md-8" v-html="product.etc_note.replace(/\n/g, '<br>')"></div>
            <br>
            <RouterLink class="btn btn-outline-secondary" :to="{ name: 'map', params:{'bank': product.kor_co_nm}}">🗺️ 가까운 {{ product.kor_co_nm }} 찾기</RouterLink>
            <br>
            <br>
            <br>
            <div class="text-center">
                
                <i class="bi" :class="isLike ? 'bi-heart-fill':'bi-heart'" @click="likeProduct"></i>
                <p>찜하기</p>
            </div>
            <p class="fs-5 col-md-8">금리</p>
            <table class="table text-center">
                <thead>
                <tr>
                    <th>구분</th>
                    <th>기간</th>
                    <th>금리</th>
                    <th>최고 금리</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="option in product.depositoption_set" :key="option.id">
                    <td>{{ option.intr_rate_type_nm }}</td>
                    <td>{{ option.save_trm }}개월</td>
                    <td>{{ option.intr_rate }}</td>
                    <td>{{ option.intr_rate2 }}</td>
                </tr>
                </tbody>
                </table>
                
        </main>
        
    </div>
</template>

<style scoped>
i{
    font-size: 50px;
}

</style>
```





```src\components\DepositList.vue
<template>
  <div>
    <table class="table">
      <thead>

        <tr class="table-info">
          <th>상품 코드</th>
          <th>은행명</th>
          <th>상품명</th>
          <th>기타</th>
        </tr>
      </thead>
      <tbody>
        <DepositListItem
        v-for="product in products"
        :key="product.id"
        :product="product"
        />
      </tbody>
    </table>
    
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'
import DepositListItem from '@/components/DepositListItem.vue'


const props = defineProps({
  type: String,
})
const store = useIndexStore()
const products = ref(null)
const options = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.url}/bank/product/${props.type}/`,
    
  })
    .then((res) =>{
      products.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})


</script>

<style scoped>

</style>
<style>

</style>
```





```src\components\DepositListItem.vue
<template>
  <tr class="border-top">
    <td>{{ product.fin_prdt_cd }}</td>
    <td>{{ product.kor_co_nm }}</td>
    <td>{{ product.fin_prdt_nm }}</td>
    <td>
      <RouterLink :to="{ name: 'ProductDetailView', params:{id: product.id}}">자세히 보기</RouterLink>
    </td>
      
  </tr>

</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import DepositOptionItem from '@/components/DepositOptionItem.vue'
const props = defineProps({
  product: Object,
})

const options = ref(props.product.depositoption_set)
</script>

<style scoped>
.option-table {
  width: 100%;
  text-align: center;

}
</style>
```




```src\components\DepositOptionItem.vue
<template>
    <tr>
      <td>{{ option.intr_rate_type_nm }}</td>
      <td>{{ option.save_trm }}</td>
      <td>{{ option.intr_rate }}</td>
      <td>{{ option.intr_rate2 }}</td>
    </tr>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  option: Object,
})

</script>

<style scoped>

</style>
```




```src\components\EconomyNewsVideo.vue
<script setup>  
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from "axios"

const apiKey = import.meta.env.VITE_VIDEO_API_KEY;
const router = useRouter()
const videos = ref([])
const searchURL = 'https://www.googleapis.com/youtube/v3/search?'
const searchTerm = '한국경제'

const params = {
        key: apiKey,
        part: 'snippet',
        q: searchTerm,
        maxResults: 6 ,
        order: 'date',
        type: 'video',
        safeSearch: "moderate",
    }
const start = () => {
  axios.get(searchURL, { params })
  .then((response) => { 
    videos.value = response.data.items
    for(var i=0; i<videos.value.length; i++){
      videos.value[i]['url'] = "https://www.youtube.com/watch?v=" + response.data.items[i].id.videoId
    }
  }).catch((error) => {
    console.error(error)
  })
}

onMounted(() => {
    start(); // 컴포넌트가 마운트되면 start 함수 실행
})

</script>

<template>
  <div class="card p-5 m-5">
    <h3>오늘의 경제 영상</h3>
    <div class="card-body">
      <div class="container">
        
        <div v-if="videos.length > 0" class="row justify-content-center row-cols-1 row-cols-m-3 g-3">
          
          <div v-for="video in videos" class="card mt-3 mb-3 mx-3" style="width: 18rem;">
            <a :href="video.url">
              <img :src="video.snippet.thumbnails.high.url" alt="" class="card-img-top">
              <div class="card-body">
                <h5 class="card-title" v-html="video.snippet.title"></h5>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
a{
  color: black;
  text-decoration: none;
}
</style>
```





```src\components\MainNavbar.vue

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { useIndexStore } from '@/stores/index'

const router = useRouter()
const store = useIndexStore()

const user = computed(() => {
  return store.user
})
const isLogin = computed(()=>{
  return store.isLogin
})
// console.log(isLogin)

const logout = ref(store.logout)

const goHome = () => {
  router.push('/')
}
const isNavbarOpen = ref(false);

const toggleNavbar = () => {
  isNavbarOpen.value = !isNavbarOpen.value;
}

const closeNavbar = () => {
  isNavbarOpen.value = false;
}

</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">
          <img alt="Pjt logo" class="logo" src="@/assets/logo_nonbackgroound.png" height="50" @click="goHome" />
        </a>
        <button class="navbar-toggler bg-light" type="button" @click="toggleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse collapse" :class="{ 'show': isNavbarOpen }" @click="closeNavbar">
          <ul class="navbar-nav nav-tabs ms-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'main' }">
                🏡메인
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'community' }">
                📢커뮤니티
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'PriceView' }">
                👑현물 상품
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'DepositView' }">
                🐷저축성 상품
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'ExchangeCalculator' }">
                💹외환 상품
              </RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'EconomyNews' }">
                📰경제뉴스
              </RouterLink>
            </li>
            <li class="nav-item" v-if="user">
              <RouterLink v-if="isLogin" class="nav-link" :to="{ name: 'ProfileView', params:{id: user}}">
                ⚙️내 정보
              </RouterLink>
            </li>
            <li class="nav-item" v-if="!isLogin">              
              <RouterLink class="nav-link" :to="{ name: 'LoginView' }" >
                🔑로그인
              </RouterLink>
            </li>
            <li class="nav-item" v-if="isLogin">
              <a class="nav-link" type="button" @click="logout">
                🔑로그아웃
              </a>
            </li>
            <li class="nav-item" v-if="!isLogin" >
              <RouterLink class="nav-link" :to="{ name: 'SignUpView' }">
                🖋️회원가입
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<style scoped>
@import '@/assets/css/bootstrap.min.css';
.logo {
  cursor: pointer;
}
.input-container {
  display: flex;
  gap: 10px; /* 좌우 간격을 조절할 값 (원하는 간격으로 조절) */
  justify-content: space-around; /* 입력 요소들을 동일한 간격으로 배치 */
  align-items: center; /* 세로 중앙 정렬을 위한 설정 */
}
.nav-link{
  color: white;
}
.nav-link:hover{
  color: rgb(187, 187, 187);
}
.router-link-exact-active, .router-link-active {
  color: rgb(187, 187, 187) !important;
}
</style>


```



```src\components\MainSurvey.vue
<!-- MainSurvey.vue -->
<template>
  <div class="container p-3">
    <h2 class="text-center p-3">당신의 투자성향은?</h2>
    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-body">
            <div v-for="(question, index) in questions" :key="index">
              <h5 class="card-title">{{ question.title }}</h5>
              <div class="form-check" v-for="(answer, answerIndex) in question.answers" :key="answerIndex">
                <input class="form-check-input" type="radio" :id="`question-${index}-answer-${answerIndex}`" v-model="selectedAnswers[index]" :value="((answerIndex+1) * question.score)">
                <label class="form-check-label" :for="`question-${index}-answer-${answerIndex}`">{{ answer }}</label>
              </div>
              <br>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 text-center">
        <button type="button" class="btn btn-secondary" @click="submit">제출</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const questions = ref([
  { title: '고객님의 투자 자금의 투자 예정 기간은 얼마나 되시나요?', 
    answers: ['6개월 이내', '6개월 ~ 1년', '1년 ~ 2년', '2년 ~ 3년', '3년 이상'],
    score: 4
},
  { title: '평소 투자경험과 가장 가까운 것을 고르세요.', 
  answers: ['예적금/국채/지방채/보증채/MMF/CMA', '금융채/회사채(신용도 상)/채권형 펀드/ELS(원금보존추구형)', '회사채(신용도 중)/ELS(원금 일부 보장)/혼합형펀드', '회사채(신용도 하)/주식/ELS(원금 미보장)/주식형펀드(시장수익률 수준의 수익)', 'ELW/선물옵션/주식형펀드(시장수익률 이상 수익)/파생상품 펀드/주식신용거래'],
  score: 4

},
  { title: '금융상품 투자에 대한 고객님의 지식수준은 어느 정도입니까?', 
  answers: ['투자의사결정을 스스로 내려본 경험이 없다', '주식과 채권의 차이를 구별할 수 있다', '투자할 수 있는 대부분의 금융차이를 구분할 수 있다.', '투자대상 상품의 차이를 이해할 수 있다'],
  score: 5,
},
  { title: '현재 투자하고자 하는 자금은 전체 금융자산 중 어느 정도 비중 차지하나요?', 
  answers: ['40%이상', '30% ~ 40%', '20% ~ 30%', '10% ~ 20%', '10% 미만'],
  score: 4
},

  { title: '고객님께서 금융상품 투자 시 감내할 수 있는 손실은 어느 정도 되시나요?', 
  answers: ['손실을 원하지 않음(무조건 원금 보전)', '원금의 30%까지 손실은 감내할 수 있음', '원금의 50%까지 손실은 감내할 수 있음', '원금 100% 손실까지 감내할 수 있음'],
  score: 5
},
//   { title: '고객님의 수입은 어느정도인가요?', 
// answers: ['', '', ''] 
// },
//   { title: '고객님의 연령대는 어떻게 되나요?', 
// answers: ['19세 이하', '20 ~ 40세', '41 ~ 50세', '51 ~ 60세', '61세 이상'] 
// },
]);

const selectedAnswers = ref([NaN, NaN, NaN, NaN, NaN]);

const submit = () => {
  // 서버로 선택된 답변을 전송하는 로직 추가

  let sum = 0
  for (let i=0; i<selectedAnswers.value.length; i++){
    sum += selectedAnswers.value[i]
  }
  if (isNaN(sum)){
    console.log(sum)
    alert('모두 선택해 주세요.')
  }else{
    router.push({
      name: 'SurveyAnswer',
      query: { selectedAnswers: sum
      },
    });
  }
};
</script>

<style scoped>
.card {
  margin-bottom: 20px;
}

.card-title {
  font-size: 20px;
}
</style>
```




```src\components\MainSurveyAnswer.vue
<!-- MainSurveyAnswer.vue -->
<template>
  <div class="container p-5">
    <div class="text-center">
      <h2 class="text-center">고객님의 투자성향은?</h2>
      <div class="card m-3">
        <div class="card-body p-5">

          <!-- 여기에 선택된 답변에 따른 결과를 표시하는 내용을 추가하세요 -->
          <h5>{{ result[0] }}</h5>
          <h3>{{ result[1] }}</h3>
          <br>
          <hr>
          <br>
          <div v-if="product">
          <h3>이런 상품을 추천합니다!</h3>
            <!-- <div v-for="p in product"> -->
              <!-- <div class="container">
                <div class="row "> -->

                  <div class="row">
                    <div class="col d-flex justify-content-center p-5" v-for="p in product" >
                      <div class="card h-100" style="width: 18rem;">
                        <img :src="p.img" class="card-img-top" alt="...">
                        <div class="card-body">
                          <h5 class="card-title">{{ p.name }}</h5>
                          <p class="card-text">{{ p.content }}</p>
                      <a class="btn btn-outline-secondary" :href="p.url">{{ p.name }}정보 보러가기</a>
                    </div>
                  <!-- </div>
                  </div> -->
                  </div>
                </div>
              </div>

              <!-- <p class="lead">
                {{ p.name }}
                <a class="btn btn-outline-secondary" :href="p.url">정보 보러가기</a>
              </p> -->



            <!-- </div> -->
          </div>
        </div>
      </div>
      <RouterLink class="btn btn-secondary" :to="{ name: 'Survey' }">다시하기</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const selectedAnswers = ref([]);
const result = ref([])
const product = ref(null)
onMounted(() => {
  if (route.query.selectedAnswers) {
    selectedAnswers.value = route.query.selectedAnswers
    
    if (selectedAnswers.value <= 25) {
      result.value = ['손실은 절대 참을수 없어! 안전이 보장되어야 도전하는', '안정형']
      product.value = products.value[0]
    }else if (selectedAnswers.value <= 40) {
      result.value = ['안정적으로 수입을 쌓아가는','안정추구형']
      product.value = products.value[1]
    }else if (selectedAnswers.value <= 60) {
      result.value = ['위험을 최소화하면서 꾸준한 성장을 목표로!', '위험중립형']
      product.value = products.value[2]
    }else if (selectedAnswers.value <= 80) {
      result.value = ['고수익을 위해 높은 위험을 감수하는', '적극투자형']
      product.value = products.value[3]
    }else{
      result.value = ['모 아니면 도! 화끈하게 투자하는', '공격투자형']
      product.value = products.value[4]
    }

  }
})

const products = ref([
  [
    {name: '예금', url: '/deposit', img: 'src/assets/deposit_2.jpg', content: '이자가 낮은 대신 입금/출금/송금이 자유로운 상품'},
    {name:'적금', url: '/saving', img: 'src/assets/deposit.jpg', content: '자금을 일정 기간동안 약정된 금리로 예치해 두는 상품'}
  ],
  [
    {name: '저축은행 상품', url: '/savingBank', img: 'src/assets/deposit.jpg', content: '일반 예/적금 보다 조금 더 높은 수익을 기대할 수 있는 상품'}
  ],
  [
    {name: '외환 상품', url: '/exchange', img: 'src/assets/money.png', content: '다른 국가의 통화나 외국 환율을 기반으로 하는 투자 상품'}
  ],
  [
    {name: '현물 상품', url: '/price', img: 'src/assets/gold.jpg', content: '물리적으로 보유하는 금, 은과 같은 상품에 투자하여 시장 가격 변동으로 이익을 얻을 수 있는 상품'}
  ],
  [
    {name: '주식', url: 'https://finance.naver.com/', img: 'src/assets/stock.jpg', content: '위험을 감내하더라도 높은 수준의 투자 수익을 얻을 수 있는 상품'}, 
    {name: '선물', url: '/price', img: 'src/assets/coffee.jpg', content: ' 미래의 특정 시점에 특정 가격으로 상품을 매매하는 투자'}
  ]
])

</script>
  
<style scoped>
img {
  height: 250px;
  object-fit: cover;  
}
</style>
```





```src\components\Price.vue
<template>
  <div class="p-3">

    
      <ul class="nav nav-tabs">
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'gold' }" @click="itemClick('gold', 0)">금</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'silver' }" @click="itemClick('silver', 1)">은</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'oil' }" @click="itemClick('oil', 2)">가솔린</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'gas' }" @click="itemClick('gas', 3)">천연가스</div>
        </li>

        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'coffee' }" @click="itemClick('coffee', 4)">커피</div>
        </li>
        <li class="nav-item">
          <div class="nav-link" :class="{ 'active': activeTab === 'corn' }" @click="itemClick('corn', 5)">옥수수</div>
        </li>

      </ul>
      <div v-if="item">
        <PriceItem :item="item" />
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'
import PriceItem from '@/components/PriceItem.vue'

const store = useIndexStore()
const items = ref([])
const item = ref(null)
const activeTab = ref('gold')
onMounted(() => {
  axios({
  method: 'get',
  url: `${store.url}/bank/price/`,
  // headers: { 
  //   Authorization: `Token ${store.token}`
  //   }
  })
    .then((res) => {
      items.value = res.data
      item.value = items.value[0]
    })
    .catch((err) => {
      console.log(err)
    })
})

const itemClick = function(itemName, n){
  activeTab.value = itemName
  item.value = items.value[n]
}
</script>

<style scoped>
.nav-link {
  color: rgb(173, 173, 173);
}
</style>
```




```src\components\PriceItem.vue
<template>
  <div class="card p-5">
    <div class="card-body d-flex flex-wrap">
      <div class="p-2 flex-grow-1">

        <h3>실시간 {{ item.name }} 시세</h3>
        <h5>{{ item.price }}</h5>
        <p>{{ item.before_price }}</p>
      </div>
      <div class="p-2 flex-fill">

        <img :src="item.graph" alt="graph">
      </div>
      
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  item: Object,
})
</script>

<style scoped>

</style>
```




```src\components\ProfileArticle.vue
<template>

    <div class="card-body">
        <p class="card-text text-start">
            <RouterLink 
                v-for="article in articles" 
                :key="article.id"
                :to="{ name: 'DetailView', params: { id: article.id }}">
                <p>{{ article.title }}</p>
            </RouterLink>
        </p>
    </div>
            
        
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()

const props = defineProps({
    'articles': Object,
})
const articles = ref(props.articles)
</script>
```



```src\components\ProfileComment.vue
<template>
    <div class="card-body">
        <p class="card-text text-start">
            <RouterLink 
                v-for="comment in comments" 
                :key="comment.id"
                :to="{ name: 'DetailView', params: { id: comment.article }}">
                <p>{{ comment.content }}</p>
            </RouterLink>
        </p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()

const props = defineProps({
    'comments': Object,
})
const comments = ref(props.comments)
</script>
```





```src\components\ProfileProduct.vue
<template>
    <div class="card-body">
        <p class="card-text text-start">
            <RouterLink 
                v-for="product in products" 
                :key="product.id"
                :to="{ name: 'ProductDetailView', params: { id: product.id }}">
                <p>[{{ product.fin_prdt_cd }}] {{ product.kor_co_nm }} : {{ product.fin_prdt_nm }}</p>
            </RouterLink>
        </p>
    </div>
            
        
        
</template>

<script setup>
import { ref } from 'vue'
import { useIndexStore } from '@/stores/index'

const store = useIndexStore()

const props = defineProps({
    'products': Object,
})
const products = ref(props.products)
</script>
```




```src\components\Propensity.vue
<script setup>
import { ref, onMounted } from 'vue'
import { useIndexStore } from '@/stores/index'
import axios from 'axios'
import { RouterLink } from 'vue-router'
const store = useIndexStore()
const username = ref(null)
const userId = ref(null)
const bank = ref(null)
const age = ref(0)
const income = ref(0)
const depositNow = ref(0)
const depositType = ref('무')
onMounted(() => {
  axios({
  method: 'get',
  url: `${store.url}/user/propensity/`,
  headers: {
    Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      username.value = res.data.user_info.username
      userId.value =  res.data.user_info.id
      bank.value = res.data.bank_info.kor_co_nm
      age.value = res.data.age
      income.value = res.data.income
      depositNow.value = res.data.deposit_now
      depositType.value = res.data.deposit_type
    })
    .catch((err) => {
      console.log(err)
    })
})

</script>

<template>
  <div class="p-5">
    <h1>{{ username }} 님의 금융 정보 </h1>
    <div class="card p-5 m-5">
      <div class="card-body fs-4">

        <p>나이 : {{ age }} 세</p>
        <p>연봉 : {{ income }} 원</p>
        <p>선호 은행 : {{ bank }}</p>
        <p>보유 금액 : {{ depositNow }} 원</p>
        <p>투자 성향 : {{ depositType }}</p>
      </div>
    </div>
    <RouterLink :to="{ name: 'PropensityUpdateView' }" class="btn btn-secondary">정보 수정</RouterLink>
  </div>
</template>
<style scoped>

</style>
```





```src\components\PropensityWrite.vue
<template>
  <div class="text-center p-5">
    <!-- <img class="m-3" src="../assets/logo_nonbackgroound.png" alt="" width="80" height="57"> -->
    <h1>정보 수정</h1>
    
    <form @submit.prevent="updatePropensity">
      <div class="card p-5 m-5">
        <div class="card-body">
          <div class="mb-3 row justify-content-center">
            <label for="age" class="col-sm-2 col-form-label">나이</label>
            <div class="col-sm-3">
              <input type="number" class="form-control" id="age" v-model="age">
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="income" class="col-sm-2 col-form-label">연봉</label>
            <div class="col-sm-3">
              <input type="number" class="form-control" id="income" v-model="income">
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="bank" class="col-sm-2 col-form-label">선호은행</label>
            <div class="col-sm-3">
              <select class="form-control" v-model="bankName" id="bank">
                <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>            
              </select>
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="type" class="col-sm-2 col-form-label">투자성향</label>
            <div class="col-sm-3">
              <select class="form-control" v-model="depositType" id="type">
                <option value="미선택">미선택</option>
                <option value="안정형">안정형</option>
                <option value="안정추구형">안정추구형</option>
                <option value="위험중립형">위험중립형</option>
                <option value="적극투자형">적극투자형</option>
                <option value="공격투자형">공격투자형</option>
              </select>
            </div>
          </div>
          <div class="mb-3 row justify-content-center">
            <label for="money" class="col-sm-2 col-form-label">보유 금액</label>
            <div class="col-sm-3">
              <input type="number" class="form-control" id="money" v-model="depositNow">
            </div>
          </div>
        </div>
      </div>
      <br>
        <button type="submit" class="btn btn-secondary">수정하기</button>
      </form>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
import { useIndexStore } from '@/stores/index'
import { useRoute, useRouter } from 'vue-router'

const store = useIndexStore()
const router = useRouter()
const route = useRoute()

const age = ref(null)
const income = ref(null)
const bankName = ref(null)
const depositNow = ref(null)
const depositType = ref(null)
const banks = ["미선택", "우리은행", "한국스탠다드차타드은행", "대구은행", "부산은행", "광주은행", "제주은행", "전북은행", "경남은행", "중소기업은행", "한국산업은행", "국민은행", "신한은행", "농협은행주식회사", "하나은행", "주식회사 케이뱅크", "수협은행", "주식회사 카카오뱅크", "토스뱅크 주식회사"]

onMounted(() =>{
  axios({
  method: 'get',
  url: `${store.url}/user/propensity/`,
  headers: {
    Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      bankName.value = res.data.bank_info.kor_co_nm
      age.value = res.data.age
      income.value = res.data.income
      depositNow.value = res.data.deposit_now
      depositType.value = res.data.deposit_type
    })
    .catch((err) => {
      console.log(err)
    })
})


const updatePropensity = function () {
  axios({
    method: 'put',
    url: `${store.url}/user/propensity/`,
    data: {
      bank_name : bankName.value,
      age : age.value,
      income : income.value,
      deposit_now : depositNow.value,
      deposit_type : depositType.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      router.push({name: 'PropensityView'})
    })
    .catch((err) => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>
```