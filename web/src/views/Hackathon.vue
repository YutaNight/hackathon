<template>
  <div class="bg-dark text-white mb-5">
    <h1 class="pt-5">HACKATHON</h1>
    <h2>テーマ：テクノロジーで中学生の頃の夢叶えてみた</h2>
    <div class="container text-start w-md-75">
      <h2>1.前提</h2>
      <div>複数領域を組み合わせて面白いことをしたい！<br class="d-md-none">(そういう名言があったような...)</div>
      <div class="row text-center">
        <div class="col-xs-12 col-md-4">
          <img src="assets/region1.png" class="img-fluid" alt="">
          <div class="text-center">
            <p>自分の趣味 (音楽,漫画,アニメなど)</p>
            <p>せっかくなら仕事でできないことを！</p>
          </div>
        </div>
        <div class="col-xs-12 col-md-4">
          <img src="assets/region2.png" class="img-fluid" alt="">
          <div class="text-center">
            <p>これまで関わったことがない領域</p>
            <p>生体データで面白いことできそう？</p>
          </div>
        </div>
        <div class="col-xs-12 col-md-4">
          <img src="assets/region3.png" class="img-fluid" alt="">
          <div class="text-center">
            <p>前から興味があった領域</p>
            <p>デバイスもいろいろ普及してそう？</p>
          </div>
        </div>
      </div>
      
      <h2 class="mt-5">2.デバイス候補</h2>
      <div>キックオフの時に聞いて面白そうだったもの</div>
      <hr>
      <div class="d-md-flex justify-content-around my-3">
        <h3 class="text-warning fw-bold">Nreal air</h3>
        <div>
          <div>
            <p>スマートグラスとしてはおそらく一番有名？</p>
            <p>自分でアプリ開発して体感できる(現状はandroid必要)</p>
            <p>lightはカメラが付いているがairはないので残念</p>
            <p>見た目はサングラスみたい(イカつくない)</p>
          </div>
        </div>
        <img src="assets/nreal.jpg" class="device-img">
      </div>
      <hr>

      <div class="d-md-flex justify-content-around my-3">
        <h3 class="text-primary fw-bold">Fitbit</h3>
        <div>
          <div>
            <p>APIで外部からヘルスケアデータ取得ができる</p>
            <p>Apple Watchよりも比較的安価</p>
            <p>Pythonで使えるモジュールもあるので開発には便利そう</p>
          </div>
        </div>
        <img src="assets/fitbit.jpg" class="device-img">
      </div>
      <hr>

      <h2 class="mt-5">3.テーマ</h2>
      <div>上記組み合わせると、もしかしてあれができるのでは...?</div>
      <div class="text-center my-3">
        <video controls playsinline src="assets/theme.mp4" poster="assets/black.jpg"></video>
      </div>
      <button
        class="btn btn-primary"
        @click="isOpen = !isOpen"
      >OPEN THE CONTENTS!</button>

      <div v-if="isOpen">
        <hr>
        <h3>What is 死神の目?</h3>
        <div class="d-md-flex justify-content-around align-items-center">
          <div>
            <p>漫画『DEATH NOTE』に出てくるもの<br>※デスノート：名前を書くとその人が死ぬ</p>
            <p>死神に自分の寿命の半分を渡すことで手に入る</p>
            <p>目に映る人の名前と寿命が見える</p>
          </div>
          <div>
            <blockquote class="py-5 px-3 text-center">
              <p>
                <img src="assets/eye.jpg" alt="">
              </p>
              <cite>出典: 漫画『DEATH NOTE』1巻</cite>
            </blockquote>
          </div>
        </div>

        <h2 class="mt-5">4.構成</h2>
        <hr>
        <h3>イメージ</h3>
        <img src="assets/diagram3.png" alt="" style="width:100%;">
        <hr>
        <h3>詳細</h3>
        <img src="assets/diagram1.png" alt="" style="width:100%;">

        <h2 class="mt-5">5.寿命計算</h2>
        <div>以下サイトに記載の情報を用いることで計算が可能になる</div>
        <blockquote class="py-5 px-3 text-center">
          <iframe src="https://www.ntv.co.jp/sekaju/onair/130608/02.html"></iframe>
          <cite href="https://www.ntv.co.jp/sekaju/onair/130608/02.html">出典: 『世界一受けたい授業』</cite>
        </blockquote>

        <p>Pythonのflaskを用いてAPI開発</p>
        <div class="text-center">
          <video
            controls
            playsinline
            src="assets/demo1.mp4"
            poster="assets/thumbnail1.jpg"
            style="object-fit:cover;"
          ></video>
        </div>
        <hr>

        <h2 class="mt-5">6.デプロイ自動化</h2>
        <p>AWS環境にデプロイする時には以下作業が必要になる</p>
        <ul>
          <li>コードの改修</li>
          <li>コンテナイメージを作成</li>
          <li>イメージをAWSのECRにpush</li>
          <li>AWSマネジメントコンソールでECSサービスの更新を行う</li>
        </ul>
        <p>毎回この作業を手動で行うのは面倒なため、AWS CodePipelineでデプロイを自動化<br>※このWEBページも対象</p>
        <div class="text-center">
          <video
            controls
            playsinline
            src="assets/demo2.mp4"
            poster="assets/thumbnail2.jpg"
          ></video>
        </div>
        <hr>
        
        <h2 class="mt-5">7.MRアプリ作成</h2>
        <div>計算した寿命をNrealにて投影するアプリをUnityで作成</div>
        <div class="text-center">
          <video
            controls
            playsinline
            src="assets/demo3.mp4"
            poster="assets/thumbnail3.jpg"
          ></video>
        </div>

        <hr>
      </div>
      <h2 class="mt-5">8.身についたこと</h2>
      <hr>
        <div class="fs-3 text-info fw-bold">
          <i class="bi bi-check-circle me-2" />flaskアプリ作成
        </div>
        <ul>
          <li>Pythonは使ったことがあったが、flaskでAPI開発をするのは初めてだった</li>
          <li>意外と簡単に作成することができたが、非機能周りについては考慮できていないので今後身につけたい</li>
        </ul>
        <div class="fs-3 text-info fw-bold">
          <i class="bi bi-check-circle me-2" />AWS
        </div>
        <ul>
          <li>少し触ったことはあったが最初から構築するのは初めて</li>
          <li>ECSやCode4兄弟はいろんな場面で利用ができそうなので、生かしていきたい</li>
        </ul>
        <div class="fs-3 text-info fw-bold">
          <i class="bi bi-check-circle me-2" />Unity
        </div>
        <ul>
          <li>名前しか聞いたことがないレベルだったが、一連の使い方を身につけることができた</li>
          <li>ゲームがどのように作られるか少し見えた気がしたので、面白みのあるゲーム作成などにも挑戦してみたい</li>
        </ul>
        <div class="fs-3 text-info fw-bold">
          <i class="bi bi-check-circle me-2" />動画編集
        </div>
        <ul>
          <li>実は一番やってみたかった領域</li>
          <li>興味を持ってもらうにはどうすればいいかという点を考えながら実施できた</li>
          <li>行き当たりばったりな編集が多かったので、正しい設計を学びたい</li>
        </ul>
      <hr>

      <h2 class="mt-5">9.やったこと詳細まとめ</h2>
      <ul>
        <li>PythonでのfitbitAPI利用</li>
        <li>flask学習 (Udemy)</li>
        <li>flaskAPI開発</li>
        <li>Vue.jsによるWEBページ作成</li>
        <li>WEB, APIコンテナイメージ作成</li>
        <li>ECSでのサービス化</li>
        <li>Route53でのドメイン取得</li>
        <li>CodeCommitでのコード管理</li>
        <li>CodePipelineによるデプロイ自動化<br class="d-md-none">w/ CodeCommit, CodeBuild, CodeDeploy</li>
        <li>Unity勉強・簡易アプリ開発 (Udemy)</li>
        <li>NRSDK (Nreal用開発キット) でのアプリ開発</li>
        <li>iMovie (フリーソフト) を用いた動画編集</li>
        <li>Final Cut Pro (有料ソフト) を用いた動画編集</li>
        <li>WEBページにおける出典記載方法調査<br class="d-md-none">(念の為)</li>
        <li>動画サムネイル画像作成</li>
      </ul>

    </div>
    <footer
      class="fixed-bottom text-start ms-5 fs-1"
      :class="{ 'text-white': limit == 0, 'text-warning': limit == 1, 'text-danger': limit == 2 }"
    >
      {{ timer }}
    </footer>
  </div>
</template>

<script>
import { onMounted, ref } from 'vue'

export default {
  setup() {
    const isOpen = ref(false)

    const timer = ref('00:00')
    const start = new Date()
    const limit = ref(0)

    const disp = () => {
      const now = new Date()
      const datet = parseInt((now.getTime() - start.getTime()) / 1000)
      let hour = parseInt(datet / 3600)
      let min = parseInt((datet / 60) % 60)
      let sec = datet % 60

      // 数値が1桁の場合、頭に0を付けて2桁で表示する指定
      if(hour < 10) hour = "0" + hour
      if(min < 10) min = "0" + min
      if(sec < 10) sec = "0" + sec

      if(min >= 10 && min < 12) limit.value = 1
      if(min >= 12) limit.value = 2

      // フォーマットを指定（不要な行を削除する）
      timer.value = min + ':' + sec
    }

    onMounted(() => {
      setInterval(disp, 1000)
    })

    return {
      isOpen,
      disp,
      timer,
      limit
    }
  }
}
</script>

<style lang="scss" scoped>
p {
  font-size: 24px;
}
.img-fluid {
  height: 120px;
  padding: 0 auto;
}

.device-img {
  width: 180px;
}

video {
  width: 80%;
  object-fit: cover;
}
div {
  font-size: 20px;
}

iframe {
  width: 100%;
  height: 600px;
}

blockquote {
  /* background-color: #fafbfc; */
  border: 1px solid #ddd;
  position: relative;
  &::before {
    font-family: serif;
    // color: gray;
    content: '“';
    font-size: 60px;
    left: 10px;
    top: 0;
    position: absolute;   
    line-height: 60px;
  }
  &::after {
    font-family: serif;
    // color: gray;
    content: '”';
    font-size: 60px;
    right: 10px;
    bottom: 0;
    position: absolute;
    line-height: 0;
  }
}

@media screen and (max-width:480px) {
  iframe {
    height: 300px;
  }
  div {
    font-size: 16px;
  }
  p {
    font-size: 14px;
    word-break: break-word;
  }
  .title {
    width: 120px;
  }
}
</style>