<template>
  <div class="wholePage" :class="{ test: isDrawOpen }">
    <div class="card-area">
      

    </div>  
    <md-divider inset></md-divider>
    <div class="infoArea">
      <h2>{{ infoAreaMessage }}</h2>
      <p :contenteditable="isEditingInfoArea" v-html="msg" class="message-content"></p>
      <md-filled-button v-if="isAdmin" class="edit-button" :class="{ 'editing': isEditingInfoArea }" @click="toggleEditingInfoArea">{{ isEditingInfoArea ? langSaveUI : langEditUI }}</md-filled-button>
    
      
        
    </div>
  </div>
</template>



<script>
import axios from 'axios';
import draggable from 'vuedraggable'


export default {
  components: {
    draggable,
  },
  props: {
    isDrawOpen: Boolean,
    showUserName: Boolean,
    customisedAppName: String,
    selectedLanguage: String,
  },
  name: 'LaunchPad',
  data() {
    return {
      fetchCards: [],

      fetchCardsStartAt1: [],
      isEditingInfoArea: false, // enable admin to edit the info area
      
      resp: [],
      apiKey: import.meta.env.VITE_API_KEY,
      isEditing: false, // enable admin to edit the info area
      isEditingAppName: false,
      isAdmin: false, // check if the user is an admin
      

      langEditUI: "",
      langSaveUI: "",
      langDefaultUI: "",
      langExitUI: "",
      infoAreaMessage: "",
      showUserMessage: "",
      infoAreaConfirm: "",
      updateMessageFail: "",
      updateMessageSuccess: "",
    };
  },
  mounted() {
    this.fetchData();
    
  },
  watch: {
    
    selectedLanguage() {
      this.getLanguage(); // Call the method to update backend
    }
  },
  methods: {
     fetchData() {
      axios.get('https://daniil-web-portfolio.onrender.com/applications/', {
        headers: {
          'X-Api-Key': this.apiKey
        }
      }).then(response => {
          this.fetchCards = response.data;

          this.getLanguage();
          //console.log('Selected Language:', this.selectedLanguage);
          
          if (this.fetchCards[0].error) {
            
            
            console.log("error: " + this.fetchCards[0].error + " " + this.fetchCards[0].code)

            this.msg = "Error "+ this.fetchCards[0].code + ": "+ this.fetchCards[0].error;
          
          } else {


            // Replace \n with <br> in the message
          let content = this.fetchCards[0].message.replace(/\n/g, '<br>');
          // Replace ## with <h3> and </h3> in the message
          content = content.replace(/## (.*?)(<br>|$)/g, '<h3>$1</h3>');
          // Repalce markdown-style links with <a> tags
          content = content.replace(/\[(.*?)\]\((#.*?)\)/g, '$1 <a href="$2">$2</a>');
          this.msg = content;

          console.log("Successfully loaded cards: 200")

          this.isAdmin = this.fetchCards[0].user_role === "True"; // set isAdmin based on the response

          this.fetchCards = response.data.map(card => ({...card, isEditingCardContent: false 
        }));
          this.fetchCardsStartAt1 = this.fetchCards.slice(1);
          console.log('Data fetched successfully:', this.fetchCards);
          }
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },

    

    
    openUrl(url, card) {
      if (!card.isEditingCardContent && !this.isEditingCardArea)
        window.open(url, '_blank');
    },

    saveEditedMessage() {
    // Send a POST request to update the message
    axios.post('https://daniil-web-portfolio.onrender.com/info/', { message: this.msg }, // Data object
    { headers: { 'X-Api-Key': this.apiKey } })
        .then(response => {
          this.resp=response.data
          if (this.resp[0].error) {     
            console.log("error: " + response.data[0].error + " " + response.data[0].code)

            !window.alert(this.updateMessageFail + " (" + response.data[0].error + " (error "+ response.data[0].code + ")");      
          } else {
            console.log('Message updated successfully: ', response.data);

            !window.alert(this.updateMessageSuccess + " (" + this.resp[0].response+ ")");
            
            // Refresh the data after successful update
            this.fetchData();
          }     
        })
        .catch(error => {
            console.error('Error updating message:', error);

            !window.alert(this.updateMessageFail + " " + error);
        });
    },

    

    toggleEditingInfoArea() {
      if (!this.isEditingInfoArea && !window.confirm(this.infoAreaConfirm)) {
        return;
      }
      this.isEditingInfoArea = !this.isEditingInfoArea;
      if (!this.isEditingInfoArea) {
        
        let content = document.querySelector('p[contenteditable]').innerHTML;
        this.msg = content;
        this.saveEditedMessage()

       
      }
    },
    
    

    


getLanguage() {
  axios.get(`https://daniil-web-portfolio.onrender.com/language/${this.selectedLanguage}`)
    .then(response => {
      console.log('Language set:', response.data);
      console.log('editUI set: ', response.data.editUI);

      this.langEditUI = response.data.editUI;
      this.langSaveUI = response.data.saveUI;
      this.langDefaultUI = response.data.defaultUI;
      this.langExitUI = response.data.exitUI;
      this.infoAreaMessage = response.data.infoMessage;
      this.showUserMessage = response.data.showUserMessage;
      this.appName = response.data.appName;
      this.infoAreaConfirm = response.data.infoAreaConfirm;
      this.exitEditCardConfirm = response.data.exitEditCardConfirm;
      this.editCardConfirm = response.data.editCardConfirm;
      this.setDefaultConfim = response.data.setDefaultConfim;
      this.editAppNameConfirm = response.data.editAppNameConfirm;
      this.updateMessageFail = response.data.updateMessageFail;
      this.updateMessageSuccess = response.data.updateMessageSuccess;
    })
}

  },
};
</script>

























<style scoped>


.h1 {


font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;




}

.h2 {


  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;




}


.h3 {


font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;




}



.wholePage {
  background-color: var(--md-sys-color-background);
  border-radius: 25px;
  padding: 20px;
  height: calc(
        100dvh - var(--topbar-height)*2 - 16px
      );
  overflow-y: auto;
  overflow-x: hidden;
}

.body{
  overflow: hidden;
}

.test {
  margin-left: 220px;
  @media screen and (max-width: 768px){
    margin-left: 50px;
  }
}

.launch-pad {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  grid-column-gap: 70px;
  grid-row-gap: 12px;
  padding-right: 40px;

}

.launch-pad .card {
  width: 100%;
  height: 140px;
  box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 1px -1px, rgba(0, 0, 0, 0.14) 0px 1px 1px 0px, rgba(0, 0, 0, 0.12) 0px 1px 3px 0px;
  border-radius: 12px;
  padding: 20px;
  background-color: var(--md-sys-color-surface-container-highest);
  cursor: pointer;
  text-align: center;
  position: relative;
}

.launch-pad .card:hover {
  background-color: var(--md-sys-color-surface-variant);
}

.card-content {
  position: relative;
  height: 100%;
}

.watermark-container {
  position: absolute;
  top: 37%;
  left: 30%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

.logo-watermark {
  width: 180px;
  opacity: var(--watermark-opacity);
  filter: invert(50%);
}

.title {
  color: var(--md-sys-color-on-surface);
}

.description {
  margin-top: 5px;
  color: var(--md-sys-color-on-surface);
}


.link {
  margin-top: 5px;
  color: var(--md-sys-color-on-surface);
  position: relative;
}

.edit-button.editing {
  background: linear-gradient(to right, #1452b0, #3AB151); 
}


.infoArea{
  color: var(--md-sys-color-on-surface);

  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}


.message-content a { 
  color: #387bd9; /* change the color of the links */
}



/* when not in mobile view, z-index of card and infoArea is adjusted higher so that it can be clicked when sidebar is opened */
@media screen and (min-width: 768px){
    .card-area, .infoArea{
      z-index: 102;
    }
    .card-area, .infoArea {
      position: relative;
    }
  }
.settings-button {
  position: absolute;
  top: -10px;
  right: -2px;
  background: none;
  border: none;
  padding: 0;
}

.move-icon {
  position: absolute;
  top: -10px;
  left: 5px;
  width: 30px;
  height: 30px;
}

.settings-button img {
  width: 32px;
  height: 30px;

}

.checkboxCard {
  position: absolute;
  top: 90px;
  left: 3px;
  width: 30px;
  height: 30px;
}

/* The switch button for showing user name or not */
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
  margin-right: 10px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:focus + .slider {
  box-shadow: 0 0 1px #2196F3;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}









</style>
