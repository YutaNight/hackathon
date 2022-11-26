import { createRouter, createWebHistory } from 'vue-router'
import Intro from '../views/Intro.vue'
import Live from '../views/Live.vue'
import Artist from '../views/Artist.vue'
import Hackathon from '../views/Hackathon.vue'

const routes = [
  {
    path: '/',
    name: 'Intro',
    component: Intro
  },
  {
    path: '/live',
    name: 'Live',
    component: Live
  },
  {
    path: '/artist',
    name: 'Artist',
    component: Artist
  },
  {
    path: '/hackathon',
    name: 'Hackathon',
    component: Hackathon
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
