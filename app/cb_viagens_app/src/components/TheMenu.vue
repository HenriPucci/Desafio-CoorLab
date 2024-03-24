<template>

  <section class="menu_content">
    <div class="menu_content_img">
      <img alt="Vue logo" src="../assets/cb_viagens_logo.png">
    </div>

    <div class="menu_content_text">
      <h3>Calculadora de Viagem</h3>
    </div>
    
    
  </section>

</template>

<script>
export default {
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.menu_content {
  display: flex;
  flex-direction: column;
  padding-left: 5%;
  width: 90%;
}

.menu_content_img {
  display: flex;
  justify-content: flex-start;
  margin-top: 10%;
  margin-bottom: 20%;
}
.menu_content_img img {
  width: 70%; 
  max-width: 100%;
}
.menu_content_text {
  display: flex;
  justify-content: center;
}
h3 {
  color: #fff;
  font-size: 1.5em;
  display: flex;
  flex-shrink: 10;
}

</style>
