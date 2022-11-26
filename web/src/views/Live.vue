<template>
  <div class="bg-dark text-white">
    <h1 class="pt-5">LIVE LIST</h1>
    <LiveList :liveData="liveData" />
    <div class="container-fluid my-5">
      <div class="mx-auto" style="width:fit-content;">
        <Rank :rank="rank[0]?rank[0].artists :'test'" class="gold"/>
        <Rank :rank="rank[1]?rank[1].artists :'test'" class="cilver"/>
        <Rank :rank="rank[2]?rank[2].artists :'test'" class="bronze"/>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, reactive, onMounted } from 'vue'
import LiveList from "@/components/LiveList"
import Rank from "@/components/Rank"
import liveMasterData from "@/assets/json/live"

export default defineComponent({
  name: "Live",
  components: {
    LiveList,
    Rank
  },
  setup() {
    const liveData = ref([])
    const count = reactive({})
    const rank = ref([])
    onMounted(() => {
      liveMasterData.forEach(yearlyLives => {
        yearlyLives.data.forEach(live => {
          if (Array.isArray(live.artists)) {
            live.artists = live.artists.join("<br>")
          }
          live.artists.split("<br>").forEach(artistName => {
            count[artistName] = (count[artistName])? count[artistName] + 1 : 1
          })
        })
        liveData.value.push(yearlyLives)
      })
      const uniueCount = [...new Set(Object.values(count))].sort().reverse()
      uniueCount.forEach(num => {
        const tmp = {
          count: num,
          artists: []
        }
        Object.keys(count).forEach(artistName => {
          if (count[artistName] == num) {
            tmp.artists.push(artistName)
          }
        })
        tmp.artists = tmp.artists.join(", ")
        rank.value.push(tmp)
      })
    })

    return {
      liveData,
      count,
      rank,
      liveMasterData,
    }
  }

})
</script>

<style scoped>
.crown {
  width: 50px;
  height: 50px;
  opacity: 1;
  margin: 0 20px 20px 0;
}
.gold {
  fill: #dab300;
}
.cilver {
  fill: #BDC3C9;
}
.bronze {
  fill: #ac6b25;
}
</style>