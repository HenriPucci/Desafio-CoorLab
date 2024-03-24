<template>
  <section class="home">
    <div class="menu_content">
      <TheMenu/>
    </div>
    <TheMain/>
  </section>
</template>

<script>
import TheMain from './components/TheMain.vue'
import TheMenu from './components/TheMenu.vue'

export default {
  name: 'App',
  components: {
    TheMenu,TheMain
  }
}
</script>

<style>
  *{
    margin: 0;
    padding: 0;
  }

  .home{
    display: flex;
    justify-content:flex-start;
    align-items: center;
    height: 100vh;
  }

  .menu_content{
    width: 20%;
    height: 100%;
    background-color: #2c2c43;
  }

</style>
