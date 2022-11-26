<template>
  <div>
    <h3
      class="p-3 m-3 bg-light"
      :class=stageName
    >{{ stageName.toUpperCase() + ' STAGE' }}
    </h3>
    <div class="box-empty-university" style="height:150px;" v-if="stageName == 'university'"></div>
    <div
      v-for="data in targetArtist"
      :key="data.artist"
    >
      <div>
        <div
          class="text-white"
          :class="'box-' + stageName"
        >
          <div
            class="artist-name"
            @click="clickName(data.artist, $event)"
            style="cursor:pointer"
          >
            {{ data.artist }}
          <ArtistDetail
            v-if="detail == data.artist"
            :positionX="positionX"
            :positionY="positionY"
            :stage="stageName"
            :artist="data.artist"
            @close = "detail = ''"
          />
          </div>
        </div>
      </div>
      <div :class="'box-empty-' + stageName"></div>
    </div>
    <div :class="'box-' + stageName" style="height:150px;" v-if="stageName != 'university'">
      <div
        class="artist-name" 
        @click="clickName(allArtist[allArtist.length-1].artist, $event)"
        style="cursor:pointer"
      >{{ allArtist[allArtist.length-1].artist }}
        <ArtistDetail
          v-if="detail == allArtist[allArtist.length-1].artist"
          :positionX="positionX"
          :positionY="positionY"
          :stage="stageName"
          :artist="allArtist[allArtist.length-1].artist"
          @close = "detail = ''"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted, computed, ref } from 'vue'
import artist from "@/assets/json/artist.json"
import ArtistDetail from "@/components/ArtistDetail"

export default defineComponent({
  components: {
    ArtistDetail,
  },
  props: {
    stage: String
  },
  setup(props) {
    const stageName = computed(() => props.stage)
    const allArtist = artist[stageName.value]
    const targetArtist = computed(() => stageName.value == 'university'? artist[stageName.value] : artist[stageName.value].slice(0, -1))

    const detail = ref("")
    const positionX = ref("")
    const positionY = ref("")
    
    const clickName = (artistName, e) => {
      detail.value = artistName
      positionX.value = String(e.pageX)
      positionY.value = String(e.pageY)
    }

    onMounted(() => {
      
    })

    return {
      allArtist,
      targetArtist,
      stageName,
      detail,
      clickName,
      positionX,
      positionY
    }
  }
})
</script>

<style scoped>
.box {
  height: 300px;
  width: 100%;
  padding: 30px;
  border: 3px solid purple;
  background-color: rgb(146, 79, 137);
}
.junior {
  color: rgb(229, 89, 178);
  border: 5px solid rgb(229, 89, 178);
  background-color: pink;
  font-weight: 900;
}
.university {
  color: blue;
  border: 5px solid blue;
  background-color: rgb(130, 192, 240);
  font-weight: 900;
}
.worker {
  color: orange;
  border: 5px solid orange;
  background-color: rgb(255, 255, 0);
  font-weight: 900;
}
.box-junior {
  background-color: rgb(236, 48, 167);
  border: 1.5px solid white;
}
.box-university {
  background-color: rgb(16, 16, 194);
  border: 1.5px solid white;
}
.box-worker {
  background-color: rgb(255, 225, 0);
  border: 1.5px solid white;
}
.box-empty-junior {
  background-color: rgb(252, 212, 219);
  border: 1.5px solid white;
  height: 200px;
}
.box-empty-university {
  background-color: rgb(149, 199, 238);
  border: 1.5px solid white;
  height: 200px;
}
.box-empty-worker {
  background-color: rgb(250, 251, 161);
  border: 1.5px solid white;
  height: 200px;
}
.artist-name {
  font-size: 30px;
  font-weight: 600;
  margin: 10px;
  padding: 10px;
}
</style>