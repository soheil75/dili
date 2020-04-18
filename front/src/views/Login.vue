<template>
<div class="container">
    <div class="row">
        <div class="col-12 col-md-6 m-md-auto">
            <img class="logo" src="../assets/logo.png" alt="diligens">
            <form @submit="onSubmit">
                <div class="col-12">
                    <label>نام کاربری</label>
                </div>
                <div class="input-group edit mb-3 col-12" :class="{shakeError:$v.LoginForm.Username.$error}">
                    <div class="input-group-prepend">
                        <span class="input-group-text edit"><i class='fas fa-user'></i></span>
                    </div>
                    <input type="text" 
                        class="form-control input-edit" 
                        @blur="$v.LoginForm.Username.$touch()" 
                        v-model="LoginForm.Username" 
                        placeholder="نام کاربری"
                        :class="{'is-invalid':$v.LoginForm.Username.$error,
                                'is-valid':!$v.LoginForm.Username.$invalid}"
                        >
                    <div class="hidden" :class="{'invalidFeedback':$v.LoginForm.Username.$error}">لطفا این فیلد را پر کنید</div>
                    <div class="hidden" :class="{'invalidFeedback':!$v.LoginForm.Username.minlin}">تعداد کاراکترها از 6 عدد نمی تواند کمتر باشد</div>
                </div>
                <div class="col-12">
                    <label>رمزعبور</label>
                </div>
                <div class="input-group mb-5 col-12" :class="{shakeError:$v.LoginForm.Password.$error}">
                    <div class="input-group-prepend">
                        <span class="input-group-text edit"><i class='fas fa-lock'></i></span>
                    </div>
                    <input type="password" 
                    @blur="$v.LoginForm.Password.$touch()" 
                    :class="{'is-invalid':$v.LoginForm.Password.$error,
                                'is-valid':!$v.LoginForm.Password.$invalid}" 
                    class="form-control input-edit" 
                    v-model="LoginForm.Password" 
                    placeholder="رمزعبور">
                    <div class="hidden" :class="{'invalidFeedback':$v.LoginForm.Password.$error}">لطفا این فیلد را پر کنید</div>
                    <div class="hidden" :class="{'invalidFeedback':!$v.LoginForm.Password.minlin}">تعداد کاراکترها از 6 عدد نمی تواند کمتر باشد</div>
                </div>
                <button type="submit" :disabled="$v.$invalid" class="btn" id="submit-btn">ورود</button>
            </form>
            <router-link id="forget-pass" to="#">رمز عبور خود را فراموش کردید؟</router-link>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import {
    required,
    minLength
} from 'vuelidate/lib/validators'

export default {
    data: () => ({
        LoginForm: {
            Username: '',
            Password: '',
        },
    }),
    methods: {
        Login(payload) {
            //const path = 'http://localhost:5000/api/login';
            const path = '/api/login';
            axios.post(path, payload)
                .then((res) => {
                    if(res.data.user){
                        this.$router.push('/AllOrder');
                    }else{
                        console.log('error1')
                    }
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
    validations: {
        LoginForm: {
            Username: {
                required,
                minlin: minLength(6)
            },
            Password: {
                required,
                minlin: minLength(6)
            },
        },
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
