<template>
  <Draggable bounds="parent">
    <div
      class="small"
      style="position: absolute; pointer-events: auto;z-index:10"
      :style="{ top: data.top, left: data.left }"
    >
      <div
        class="card bg-dark border-light content-width"
        :style="{ height: data.height }"
      >
        <div class="card-header small text-start text-white bg-secondary">
          <div class="row">
            <div class="col-11">
              {{ props.title }}
            </div>
          </div>
        </div>
        <div class="card-body text-start text-white">
          <slot></slot>
          <div class="mt-1 text-center">
            <button
              type="button"
              class="btn btn-sm btn-secondary center"
              @click="$emit('close-dialog')"
              @touchend="$emit('close-dialog')"
            >
              閉じる
            </button>
          </div>
        </div>
      </div>
    </div>
  </Draggable>
</template>

<script>
import { defineComponent, onMounted, reactive } from "vue";
// モードレスダイアログのモジュール(https://github.com/bcakmakoglu/revue-draggable)
import { Draggable } from "@braks/revue-draggable";

export default defineComponent({
  components: {
    Draggable,
  },

  props: {
    title: { type: String, default: "" },
    width: { type: String, default: "16rem" },
    positionTop: { type: String, default: "45%" },
    positionLeft: { type: String, default: "40%" },
  },

  emits: ["close-dialog", "full-screen", "stack-screen"],

  setup(props) {
    const data = reactive({
      width: "",
      height: "",
      top: "",
      left: "",
    });
    onMounted(async () => {
      data.width = props.width;
      data.top = props.positionTop;
      data.left = props.positionLeft;
      if (screen.width < 500) {
        data.left = "20%"
      }
    });
    return {
      props,
      data,
    };
  },
});
</script>

<style scoped>
.content-width {
  width: 600px;
}
@media screen and (max-width:480px) {
  .content-width {
    width: 300px;
  }
}
</style>
