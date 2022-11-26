<template>
  <div>
    <h1 class="header">Naitoの部屋</h1>
    <button type="button" class="menu-btn btn btn-secondary" v-on:click="open=!open">
      <i class="bi bi-list" style="font-size:30px;"></i>
    </button>
    <div class="menu" v-bind:class="{'is-active' : open }">
      <div class="menu__item" @click="goPage('Intro')">INTRODUCTION</div>
      <div class="menu__item" @click="goPage('Live')">LIVE</div>
      <div class="menu__item" @click="goPage('Artist')">ARTIST</div>
      <div class="menu__item" @click="goPage('Hackathon')">HACKATHON</div>
    </div>
    <router-view/>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  setup() {
    const router = useRouter()

    const open = ref(false)

    const goPage = pageName => {
      open.value = !open.value
      router.push({ name: pageName })
    }

    return {
      open,
      goPage
    }
    
  },
})
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.header {
  height: 100px;
  text-align: start;
  padding: 20px;
  background-color: #330066;
  margin: 0;
  color: white;
}
#nav {
  padding: 30px;
  background-color: #330066;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
/*----------------------------
* メニュー開閉ボタン
*----------------------------*/
.menu-btn {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 3;
  background: #333;
  color: #fff;
  width: 60px;
}

/*----------------------------
* メニュー本体
*----------------------------*/
.menu {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1;
  width: 30vw;
  height: 100vh;
  justify-content: center;
  background: rgba(94, 6, 94, 0.794);
  padding: 100px 0;
}
.menu__item {
  padding: .5em 1em;
  text-align: start;
  color: #fff;
  cursor: pointer;
  font-size: 1.5rem;
}

/*----------------------------
* アニメーション部分
*----------------------------*/

/* アニメーション前のメニューの状態 */
.menu {
  transform: translateX(100vw);
  transition: all .3s linear;
}
/* アニメーション後のメニューの状態 */
.menu.is-active {
  transform: translateX(80vw);
}

@media screen and (max-width:480px) {
  .menu {
    width: 100vw;
    height: 50vh;
    /* display: none; */
  }
  .menu.is-active {
    transform: translateX(0);
  }
}
</style>
