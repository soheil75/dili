<template>
<div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6 m-md-auto">
                <Header :title="title" :link="backlink"></Header>
                <div class="info">
                    <img :src="require(`@/assets/${ware.imagePath}`)" :alt="ware.Title">
                    <h4 class="ware-name">{{ware.Title}}</h4>
                    <div class="divider"></div>
                    <h4 class="route font-14 pt-0"><i class="fal fa-flip-horizontal p-2 fa-plane-departure"></i>مبدا : <span>{{ware.Origin}}</span></h4>
                    <h4 class="route font-14 pt-0"><i class="fal fa-flip-horizontal p-2 fa-plane-arrival"></i>مقصد : <span>{{ware.Destination}}</span></h4>
                    <div class="divider"></div>
                    <h4 class="title">تاریخ تحویل کالا : <span>{{ware.Date}}</span></h4>
                    <h4 class="title font-13 red-color" v-if="!ware.Accept"><i class="fal fa-exclamation-triangle pl-2"></i>عدم دریافت کالا بعد از تاریخ فوق</h4>
                    <div class="divider"></div>
                    <h4 class="title">توضیحات کالا</h4>
                    <p class="font-12 px-4">{{ware.Description}}</p>
                    <div class="divider"></div>
                    <a class="btn w-50 info-button link-button" :href="ware.Url">مشاهده کالا</a>
                    <div class="divider"></div>
                    <div class="pass-info mb-4 pb-1">
                        <form @submit="onSubmit">
                            <div class="col-12">
                                <h4 class="title">تاریخ تحویل کالا</h4>
                            </div>
                            <div class="input-group mb-4 col-12">
                                <date-picker @input="$v.Date.$touch()" v-model="comments.date" format="YYYY-MM-DD" display-format="dddd jDD jMMMM jYYYY" :auto-submit="true" placeholder="تاریخ تحویل کالا انتخاب کنید" input-class="form-control w-100" color="#b8221f" style="width:100%" :min='min' required/>
                            </div>
                            <div class="col-12">
                                <h4 class="title">مبلغ پیشنهادی</h4>
                            </div>
                            <div class="input-group mb-4 col-12">
                                <input type="number" @blur="$v.Cost.$touch()" v-model="comments.cost" class="form-control" placeholder="مبلغ پیشنهادی" required>
                            </div>
                            <div class="form-group mb-4 col-12">
                                <h4 class="title">توضیحات شما</h4>
                                <textarea @blur="$v.Text.$touch()" v-model="comments.text" class="form-control" placeholder="توضیحات" required></textarea>
                            </div>
                            <button type="submit" class="btn submit-btn">ثبت پیشنهاد</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import Header from '@/components/Header.vue'
import datePicker from 'vue-persian-datetime-picker';
import axios from 'axios'
import { required } from 'vuelidate/lib/validators'

export default {
    components: {
        Header,
        datePicker,
    },
    data() {
        return {
            title: 'جزییات درخواست',
            backlink: '/AllOrderPass',
            ware: '',
            comments: {
                date: null,
                cost: null,
                text: '',
            }
        }
    },
    methods: {
        getMinData() {
            var todayDate = new Date().toISOString().slice(0, 10);
            this.min = todayDate
        },
        getware() {
            const path = `/api/acceptOrder/${this.$route.params.id}`;
            axios.get(path)
                .then((res) => {
                    this.ware = res.data.ware;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        accept(payload) {
            const path = `/api/acceptOrder/${this.ware.id}`;
            axios.post(path, payload)
                .then(() => {
                    this.$router.push('/MySuggestionsPass');
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.log(error);
                });
        },
        onSubmit(evt) {
            evt.preventDefault();
            const payload = {
                date: this.comments.date,
                cost: this.comments.cost,
                text: this.comments.text,
            };
            this.accept(payload);
            this.initForm();
        },
        initForm() {
            this.comments.date = null;
            this.comments.cost = null;
            this.comments.text = '';
        },
    },
    created() {
        this.getware();
        this.getMinData();
    },
    validations: {
        Date: {
            required,
        },
        Cost: {
            required,
        },
        Text: {
            required,
        }
    }
}
</script>
