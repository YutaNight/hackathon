<template>
  <div>
    <div
      class="container"
      v-for="yearlyLives in innerLiveData"
      :key="yearlyLives.year"
    >
      <h2 class="text-start ml-2">{{ yearlyLives.year }}</h2>
      <table class="table table-striped table-light table-bordered text-start">
        <thead>
          <tr>
            <th scope="col">日程</th>
            <th scope="col">タイトル</th>
            <th scope="col" class="d-none d-lg-table-cell">会場</th>
            <th scope="col">アーティスト</th>
          </tr>
        </thead>
        <tbody>
          <tr 
            v-for="live in yearlyLives.data"
            :key="live.date"
          >
            <td>{{ live.date }}</td>
            <td>{{ live.title }}</td>
            <td class="d-none d-lg-table-cell">{{ live.venue }}</td>
            <td v-html="live.artists"></td>
          </tr>
        </tbody>
      </table>
      <h3 class="text-end mr-2">TOTAL: {{ yearlyLives.data.length }}</h3>
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from 'vue'

export default defineComponent({
  name: "LiveList",
  props: {
    liveData: Array
  },
  setup(props) {
    const innerLiveData = computed(() => props.liveData)

    return {
      innerLiveData,
    }
  }
})
</script>

<style>
th {
  word-break: keep-all;
}
table {
  font-size: 18px;
}
@media screen and (max-width: 480px){
  table {
    font-size: 10px;
  }
}
</style>