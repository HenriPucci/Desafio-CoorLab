<template>
  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  </head>

  <section class="main">

    <div class="main_top"></div>

    <section class="main_box">

      <div class="main_box_content">

        <div class="main_box_content_top">
          <i class="fas fa-truck"></i>

          <h3>Calculadora de Viagem</h3>
        </div>
        <div class="main_box_content_text">
          <div class="input_boxes">
            <span class="input_boxes_title">
              <i class="fas fa-money-bill"></i>
              <h3>Calcule o Valor da Viagem</h3>
            </span>
            <span class="input_boxes_text">
              <p>Destino:</p>
            </span>
            <select v-model="selectedDestiny" class="select">
              <option value="" disabled selected >
                <p class="select_label">Selecione um destino</p>
              </option>
              <option v-for="destiny in destinys" :key="destiny" :value="destiny">{{ destiny }}</option>
            </select>
            <span class="input_boxes_text">
              <p>Data:</p>
            </span>
            <input type="date" v-model="selectedDate" class="date_input">


            <button @click="searchTrips" class="search_button">Buscar</button>
          </div>
          <div class="output_boxes">
            
            <div class="fast_box" v-if="fastTrip.bed">
              <div class="fast_box_left">
                <div class="fast_box_icon">
                  <i class="fas fa-money-bill"></i>
                </div>
                <div class="fast_box_text">
                  <h2>{{ fastTrip.name }}</h2>
                  <p v-if="fastTrip.bed"> Leito{{ fastTrip.bed }}</p>
                  <p v-if="fastTrip.duration"> Tempo estimado: {{ fastTrip.duration }}</p>
                </div>
              </div>
              <div class="fast_box_right">
                <h2 v-if="fastTrip.price_confort"> Preço:</h2>
                <p>{{ fastTrip.price_confort }}</p>
              </div>
            </div>
            <div class="economic_box" v-if="economicTrip.bed">
              <div class="economic_box_left">
                <div class="economic_box_icon">
                  <i class="fas fa-clock"></i>
                </div>
                <div class="economic_box_text">
                  <h2>{{ economicTrip.name }}</h2>
                  <p v-if="economicTrip.bed"> Leito{{ economicTrip.bed }}</p>
                  <p v-if="economicTrip.duration"> Tempo estimado: {{ economicTrip.duration }}</p>
                </div>
              </div>
              <div class="economic_box_right">
                <h2 v-if="economicTrip.price_econ"> Preço:</h2>
                <p>{{ economicTrip.price_econ }}</p>
              </div>
            </div>
            <div v-if="!fastTrip.name && !economicTrip.name" class="no-data">
              <h3>Nenhum Dado Selecionado</h3>
            </div>
          </div>
        </div>
      
      </div>
    </section>

  </section>
  <div v-if="showAlert" class="alert">
    <i class="fas fa-exclamation-circle"></i>
    <p>Insira os valores para realizar a cotação.</p>
    <button @click="closeAlert">Fechar</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      destinys: [],
      selectedDestiny: '',
      selectedDate: '',
      fastTrip: {},
      economicTrip: {},
      showAlert: false
    };
  },
  mounted() {
    this.searchDestinys();
  },
  methods: {
    async searchDestinys() {
      try {
        const response = await fetch('http://localhost:3000/destinys');
        const data = await response.json();
        this.destinys = data.destinys;
      } catch (error) {
        console.error('Erro ao buscar destinos:', error);
      }
    },
    async searchTrips() {
      if (!this.selectedDestiny || !this.selectedDate) {
        this.showAlert = true;
        return;
      }
      
      try {
        const response = await fetch(`http://localhost:3000/trips?destiny=${this.selectedDestiny}`);
        const data = await response.json();
        this.fastTrip = data.confortable_trip;
        this.economicTrip = data.economic_trip;
      } catch (error) {
        console.error('Erro ao buscar viagens:', error);
      }
    },
    closeAlert() {
      this.showAlert = false;
    }
  }
};
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
  justify-content: flex-start;
  background-color: #2c2c43;
}

.main_box_content_top h3{
  color: #fff;
  font-size: 1.3em;
  margin-left: 2%;
}

.main_box_content_top i{
  color: #fff;
  font-size: 2em;
  margin-left: 5%;
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
  width: 40%;
  height: 80%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f1f1f2;
  border-radius: 5%;
}

.input_boxes_title{
  height: 20%;
  width: 80%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.input_boxes_title i{
  margin: 2%;
}

.select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 10px;
  font-size: 90%;
  background-color: #fff;
  cursor: pointer;
  width: 70%;
}

.date_input {
  padding: 10px;
  font-size: 1em;
  cursor: pointer;
  width: 65%;
  margin-top: 10px;
}

.search_button:hover {
  background-color: #0caab3;
}
.search_button {
  padding: 10px 20px;
  font-size: 1em;
  background-color: #0caab3;
  color: #000000;
  border: none;
  cursor: pointer;
  margin-top: 10px;
  width: 70%;
}

.output_boxes {
  width: 50%;
  height: 80%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.fast_box{
  width: 80%;
  height: 25%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  border-radius: 5%;

}

.fast_box_left{
  border-radius: 5%;
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

.fast_box_text{
  border-radius: 5%;
  background-color: #f1f1f2;
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;

}

.fast_box_text h2{
  font-size: 100%;
  padding-left: 10%;
}

.fast_box_text p{
  font-size: 1.0em;
  padding-left: 10%
}
.fast_box_icon{
  border-radius: 5%;
  width: 20%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #0caab3;
}

.fast_box_left i{
  font-size: 2em;
  color: #ffffff;

}

.fast_box_right{
  border-radius: 5%;
  background-color: #f1f1f2;
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 10%;
}

.fast_box_right h2{
  font-size: 100%;
  padding-left: 10%;

}

.fast_box_right p{
  font-size: 1.0em;
  padding-left: 10%
}

.input_boxes_text {
  width: 70%;
  height: 5%;
  margin-top: 5%
}

.economic_box{
  width: 80%;
  height: 25%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  border-radius: 5%;

}

.economic_box_left{
  border-radius: 5%;
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

.economic_box_text{
  border-radius: 5%;
  background-color: #f1f1f2;
  width: 80%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;

}

.economic_box_text h2{
  font-size: 100%;
  padding-left: 10%;
}

.economic_box_text p{
  font-size: 1.0em;
  padding-left: 10%
}

.economic_box_icon{
  border-radius: 5%;
  width: 20%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #0caab3;
}

.economic_box_left i{
  font-size: 2em;
  color: #ffffff;

}

.economic_box_right{
  border-radius: 5%;
  background-color: #f1f1f2;
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 10%;
}

.economic_box_right h2{
  font-size: 100%;
  padding-left: 10%;

}

.economic_box_right p{
  font-size: 1.0em;
  padding-left: 10%
}

.no-data {
  width: 80%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.alert {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 25%;
  height: 25%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
  z-index: 9999;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.alert i {
  font-size: 200%;
  color: #0caab3;
}

.alert p {
  margin-bottom: 5px;
  width: 50%;
  font-size: 110%;
  display: flex;
  align-items: center;
}

.alert button {
  padding: 5px 10px;
  width: 40%;
  background-color: #0caab3;
  color: #000000;
  border: none;
  cursor: pointer;
  border-radius: 3px;
}

</style>
