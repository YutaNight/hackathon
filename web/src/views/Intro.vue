<template>
  <div class="container-fluid bg-dark text-white px-5">
    <h1 class="pt-5">INTRODUCTION</h1>
    <div class="row mx-5 my-5">
      <div class="col-xs-12 col-sm-12 col-md-3 col-lg-3">
        <img src="assets/me.jpg" class="img-fluid" alt="">
      </div>
      <div class="col-xs-12 col-sm-12 col-md-9 col-lg-9 text-start position-relative" style="font-size:30px;">
        <p><span class="title">NAME</span><br class="d-md-none d-lg-none">内藤裕太</p>
        <p><span class="title">FROM</span><br class="d-md-none d-lg-none">福岡県大野城市</p>
        <p><span class="title">BIRTH</span><br class="d-md-none d-lg-none">1994年9月14日 (満{{ age }}歳)</p>
        <p><span class="title">GRADUATED</span><br class="d-md-none d-lg-none">九州大学システム情報科学府</p>
        <p><span class="title">HOBBY</span><br class="d-md-none d-lg-none">音楽鑑賞, ライブ参戦, アニメ鑑賞</p>
        <p>
          <span class="title">STRENGTHS</span>
          <br class="d-md-none d-lg-none">
          <span class="badge bg-success mx-1">回復思考</span>
          <span class="badge bg-danger mx-1">調和性</span>
          <span class="badge bg-primary mx-1">内省</span>
          <span class="badge bg-success mx-1">慎重さ</span>
          <span class="badge bg-primary mx-1">収集心</span>
        </p>
        <p><span class="title">SKILL</span><br class="d-md-none d-lg-none">html, css, JavaScript, vue, Python, SQL, AWS, etc</p>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    const birthday = {
      year: 1994,
      month: 9,
      date: 14
    }
    const today = new Date()
    const thisYearBirthday = new Date(today.getFullYear(), birthday.month-1, birthday.date)
    const tmp = today.getFullYear() - birthday.year
    const age = today >= thisYearBirthday? tmp : tmp - 1

    return {
      age
    }
  }
})
</script>

<style>
p {
  font-size: 24px;
}
.title {
  background-color: purple;
  border-radius: 30px;
  display: inline-block;
  width: 200px;
  text-align: center;
  font-weight: 500;
  margin: 10px;
}

@media screen and (max-width:480px) {
  p {
    font-size: 16px;
    word-break: keep-all;
  }
  .title {
    width: 120px;
  }
}
</style>