<template>
<div class="container">
    <div class="row">
        <div class="col-12 col-md-6 m-md-auto">
            <img class="logo" src="../assets/logo.png" alt="diligens">
            <form @submit="onSubmit">
                <div class="col-12">
                    <label>نام کاربری</label>
                </div>
                <div class="input-group edit mb-4 col-12">
                    <div class="input-group-prepend">
                        <span class="input-group-text edit"><i class='fas fa-user'></i></span>
                    </div>
                    <input type="text" class="form-control input-edit" v-model="LoginForm.Username" placeholder="نام کاربری" required>
                    
                </div>
                <div class="col-12">
                    <label>رمزعبور</label>
                </div>
                <div class="input-group mb-5 col-12">
                    <div class="input-group-prepend">
                        <span class="input-group-text edit"><i class='fas fa-lock'></i></span>
                    </div>
                    <input type="password" class="form-control input-edit" v-model="LoginForm.Password" placeholder="رمزعبور" required>
                    
                </div>
                <button type="submit" class="btn" id="submit-btn">ورود</button>
            </form>
            <router-link id="forget-pass" to="#">رمز عبور خود را فراموش کردید؟</router-link>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import {required,minLength} from 'vuelidate/lib/validators'
export default {
    data: () => ({
        LoginForm: {
            Username: '',
            Password: '',
        },
    }),
    methods: {
        Login(payload) {
            const path = 'http://localhost:5000/login';
            axios.post(path, payload)
                .then(() => {
                    //console.log(res.data.message)
                    this.$router.push('/AllOrder');
                    //if(res.data.message){
                    //    this.$router.push('/AllOrder');
                    //}else{
                    //    this.$router.push('/Login');
                    //}
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        onSubmit(evt) {
            evt.preventDefault();
            const payload = {
                Username: this.LoginForm.Username,
                Password: this.LoginForm.Password,
            };
            this.Login(payload);
            this.initForm();
        },
        initForm() {
            this.LoginForm.Username = '';
            this.LoginForm.Password = '';
        },
    },
    validations:{
        Username:{
            required
        },
        Password:{
            required,
            minlin:minLength(6)
        }
    }
}
</script>

<style>
.edit {
    border-top-left-radius: 0 !important;
    border-bottom-left-radius: 0 !important;
    border-top-right-radius: .25rem !important;
    border-bottom-right-radius: .25rem !important;
}

.input-edit {
    border-top-left-radius: .25rem !important;
    border-bottom-left-radius: .25rem !important;
    border-top-right-radius: 0 !important;
    border-bottom-right-radius: 0 !important;
}

#forget-pass {
    text-align: center;
    display: block;
    border-bottom: 1px dashed #00BCD4;
    color: #00BCD4;
    margin: 20px auto;
    width: fit-content;
}

#submit-btn {
    background: linear-gradient(to left, #b8221f, #e64135);
    box-shadow: 0px 3px 6px #b59d9c;
    padding: 7px 45px;
    display: block;
    margin: 15px auto 30px;
    color: #fff;
    border-radius: 4px;
    width: 50%;
}

.logo {
    max-width: 60%;
    background: #fff;
    height: auto;
    display: block;
    margin: 70px auto;
    min-width: 180px;
}
</style>
