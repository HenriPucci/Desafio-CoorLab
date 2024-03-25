<template>

  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  </head>

  <section class="menu_content">
    <div class="menu_content_img">
      <img alt="Vue logo" src="../assets/cb_viagens_logo.png">
    </div>

    <div class="menu_content_text">
      <i class="fas fa-calculator"></i>
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
  width: 90%;
}

.menu_content_img {
  display: flex;
  justify-content: flex-start;
  margin-top: 10%;
  margin-bottom: 20%;
  padding-left: 10%;
}
.menu_content_img img {
  width: 70%; 
  max-width: 100%;
}
.menu_content_text {
  display: flex;
  justify-content: flex-start;
}
h3 {
  color: #fff;
  font-size: 100%;
  display: flex;
  flex-shrink: 10;
}
i {
  color: #fff;
  font-size: 100%;
  display: flex;
  margin-left: 10%;
  margin-right: 5%;
  flex-shrink: 10;
}

</style>
