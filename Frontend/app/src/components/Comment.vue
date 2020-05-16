<template>
    <div class="container">
        <div class="row">
            <div v-if="user.isLogged == true" class="col">
                <textarea class="form-control" 
                    v-model="commentUser"
                    placeholder="Añade un comentario..."
                    rows="4"
                    max-rows="6"
                    maxlength="5000"></textarea>
                    <button class="btn btn-danger">Comentar</button>
            </div>
            <div class="col col-12">
                <h3>Comentarios</h3>
            </div>
            <div class="col col-12">
                <div v-bind:key="comment.id" v-for="comment in comments">
                    <div class="profile-comment">
                        <div>
                        <img src="@/assets/user.png" width="32" alt="">
                        </div>
                        <div>
                        <p><strong>{{comment.user}}</strong></p>
                        </div>
                    </div>
                    <div>
                        <p>{{comment.content}}</p>
                    </div>
                    <div class="interation-comment">
                        <img v-on:click="changeAction(comment.id, 1)" v-if="comment.useraction ==  0 || comment.useraction == 2" class="like" src="@/assets/like(4).png" width="32" alt="like">
                        <img v-on:click="changeAction(comment.id, 0)" v-if="comment.useraction ==  1" class="like" src="@/assets/like(3).png" width="32" alt="like">
                        <span class="content-comment">{{comment.likes}}</span>
                        <img v-on:click="changeAction(comment.id, 2)" v-if="comment.useraction ==  0 || comment.useraction ==  1" class="unlike" src="@/assets/like(4).png" width="32" alt="unlike">
                        <img v-on:click="changeAction(comment.id, 0)" v-if="comment.useraction ==  2" class="unlike" src="@/assets/like(3).png" width="32" alt="unlike">
                        <span class="content-comment">{{comment.unlikes}}</span>
                    </div>  
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import config from '@/config/configproject.js'

export default {
    data() {
        return{
            commentUser: "",
            comments: [
        {id: 1,
        user: "Pepito perez",
        date: "2020/01/03",
        likes: 5,
        unlikes: 5,
        useraction: 1,
        reports: 0,
        content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae optio sequi magni officia molestias. Nostrum aperiam, veritatis sint pariatur eveniet, voluptatem libero sunt atque voluptas quas eligendi error repellat ab.Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae optio sequi magni officia molestias."},
        {id: 2,
        user: "Pepito1215",
        date: "2020/28/02",
        likes: 10,
        unlikes: 5,
        useraction: 2,
        reports: 0,
        content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae optio sequi magni officia molestias. Nostrum aperiam, veritatis sint pariatur eveniet, voluptatem libero sunt atque voluptas quas eligendi error repellat ab."},
        {id: 3,
        user: "Destroyer123456",
        date: "2020/25/02",
        likes: 1,
        unlikes: 5,
        useraction: 0,
        reports: 0,
        content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae optio sequi magni officia molestias. Nostrum aperiam, veritatis sint pariatur eveniet, voluptatem libero sunt atque voluptas quas eligendi error repellat ab.Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae optio sequi magni officia molestias. Nostrum aperiam, veritatis sint pariatur eveniet, voluptatem libero sunt atque voluptas quas eligendi error repellat ab.Lorem ipsum dolor sit amet consectetur adipisicing e"},
        {id: 4,
        user: "Tumadre",
        date: "2020/21/02",
        likes: 5,
        unlikes: 5,
        useraction: 1,
        reports: 1,
        content: "Lorem ipsum dolor sit amet consectetur adipisicing elit. Molestiae optio sequi magni officia molestias. Nostrum aperiam, veritatis sint pariatur eveniet, voluptatem libero sunt atque voluptas quas eligendi error repellat ab."}
      ],
        }
    },
    methods: {
        changeAction(id, type) {
            for(var i=0; i<this.comments.length; i++){
                if(this.comments[i].id == id){

                if(this.comments[i].useraction == 0){
                    
                    if(type == 1){
                    this.comments[i].likes += 1
                    }
                    else {
                    this.comments[i].unlikes += 1
                    }
                }
                else if (this.comments[i].useraction == 1){
                    if(type == 0){
                    this.comments[i].likes -= 1
                    }
                    else {
                    this.comments[i].likes -= 1
                    this.comments[i].unlikes += 1
                    }
                }
                else{
                    if(type == 0){
                    this.comments[i].unlikes -= 1
                    }
                    else {
                    this.comments[i].likes += 1
                    this.comments[i].unlikes -= 1
                    }
                }

                this.comments[i].useraction = type

                break;
                }
            }
        }
    },
    computed: {
        ...mapState(['user'])
    }

}
</script>

<style>
.unlike{
  transform: rotate(180deg);;
}

.like, .unlike{
  margin-bottom: 10px;
  cursor: pointer;
}

.content-comment{
  margin-left: 10px;
  margin-right: 10px;
}

.profile-comment{
  margin-top: 10px;
}

.profile-comment div{
  display: inline-block;
}

.button-newcomment{
  margin-top: 10px;
  margin-right: 10px;
  margin-bottom: 40px;
}
</style>