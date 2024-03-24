<template>
  <section class="main">

    <div class="main_top"></div>

    <section class="main_box">

      <div class="main_box_content">

        <div class="main_box_content_top">
          <h3>Calculadora de Viagem</h3>
        </div>
        <div class="main_box_content_text">
          <div class="input_boxes">
            
          </div>
          <div class="output_boxes"></div>
        </div>
      
      </div>
    </section>

  </section>
</template>

<script>
export default {
 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

*{
    margin: 0;
    padding: 0;
  }

.main {
  display: flex;
  flex-direction: column;
  width: 100%;
  height: 100%; 
}

.main_top {
  width: 100%;
  height: 10%;
  position: fixed;
  background-color: #ffffff;
  box-shadow: 0px 10px 10px -5px rgba(0, 0, 0, 0.466);
}

.main_box {
  display: flex;
  justify-content: center;
  width: 100%;
  height:100%;
  background-color: #ffffff;
}

.main_box_content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 80%;
  height: 70%;
  margin: 10%;
  background-color: #ffffff;
  box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.404);
}

.main_box_content_top {
  width: 100%;
  height: 10%;
  display: flex;
  align-items: center;
  background-color: #2c2c43;
}

.main_box_content_top h3{
  color: #fff;
  font-size: 1.3em;
}

.main_box_content_text {
  width: 100%;
  height: 90%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.input_boxes {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: bisque;
}

.output_boxes {
  width: 50%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
