<template>
<div class="container">
    <div class="row">
        <div class="col-12 col-md-6 m-md-auto">
            <Header :title="title" :link="backlink"></Header>
            <div class="new-order">
                <form @submit="onSubmit">
                    <div class="form-group mb-4 col-12" :class="{shakeError:$v.wares.Title.$error}">
                        <label>نام کالا</label>
                        <input type="text" 
                            v-model="wares.Title" 
                            @blur="$v.wares.Title.$touch()"
                            class="form-control" 
                            placeholder="نام کالا"
                            :class="{'is-invalid':$v.wares.Title.$error,
                                'is-valid':!$v.wares.Title.$invalid}"
                        >
                        <div class="hidden" :class="{'invalidFeedback':$v.wares.Title.$error}">لطفا این فیلد را پر کنید</div>
                    </div>
                    <div class="form-group mb-4 col-12" :class="{shakeError:$v.wares.Origin.$error}">
                        <label>مبدا</label>
                        <input type="text" 
                            v-model="wares.Origin" 
                            @blur="$v.wares.Origin.$touch()" 
                            :class="{'is-invalid':$v.wares.Origin.$error,
                                'is-valid':!$v.wares.Origin.$invalid}"
                                 class="form-control" placeholder="مبدا">
                            <div class="hidden" :class="{'invalidFeedback':$v.wares.Origin.$error}">لطفا این فیلد را پر کنید</div>
                    </div>
                    <div class="form-group mb-4 col-12" :class="{shakeError:$v.wares.Destination.$error}">
                        <label>مقصد</label>
                        <input type="text" @blur="$v.wares.Destination.$touch()" v-model="wares.Destination"
                         :class="{'is-invalid':$v.wares.Destination.$error,
                                'is-valid':!$v.wares.Destination.$invalid}"
                         class="form-control" placeholder="مقصد">
                        <div class="hidden" :class="{'invalidFeedback':$v.wares.Destination.$error}">لطفا این فیلد را پر کنید</div>
                    </div>
                    <div class="col-12">
                        <label>لینک کالا</label>
                    </div>
                    <div class="input-group mb-4 col-12" :class="{shakeError:$v.wares.Url.$error}">
                        <input type="url" class="form-control"
                        v-model="wares.Url"  
                        @blur="$v.wares.Url.$touch()"
                        :class="{'is-invalid':$v.wares.Url.$error,
                                'is-valid':!$v.wares.Url.$invalid}"
                        placeholder="لینک کالا">
                        <div class="input-group-prepend">
                            <span class="input-group-text"><i class='fas fa-link'></i></span>
                        </div>
                        <div class="hidden" :class="{'invalidFeedback':$v.wares.Url.$error}">لطفا این فیلد را پر کنید</div>
                    </div>
                    <div class="form-group mb-4 col-12">
                        <label>تصویر کالا</label>
                        <div class="custom-file">
                            <label class="custom-file-label" for="inputFile" style="padding-right: 80px;"></label>
                            <input type="file" accept="image/*" class="custom-file-input" @change="onFileChange" name="image" id="inputFile" aria-describedby="inputFile" required />
                        </div>
                        <div id="preview">
                            <img v-if="previewimage" :src="previewimage" />
                        </div>
                    </div>
                    <div class="col-12 mb-4 control-box">
                        <label for="sb-inline">تعداد</label>
                        <b-form-spinbutton style="width: 40%;" class="text-center" id="sb-inline" v-model="wares.Value" min="1" step="1" max="1000" inline>
                        </b-form-spinbutton>
                    </div>
                    <div class="form-group mb-4 col-12" :class="{shakeError:$v.wares.Description.$error}">
                        <label>توضیحات کالا</label>
                        <textarea class="form-control" 
                            v-model="wares.Description" 
                            @blur="$v.wares.Description.$touch()"
                            :class="{'is-invalid':$v.wares.Description.$error,
                                    'is-valid':!$v.wares.Description.$invalid}"
                            placeholder="توضیحات">
                        </textarea>
                        <div class="hidden" :class="{'invalidFeedback':$v.wares.Description.$error}">لطفا این فیلد را پر کنید</div>
                    </div>
                    <div class="col-12">
                        <label>تاریخ دریافت کالا</label>
                    </div>
                    <div class="input-group mb-4 col-12" :class="{shakeError:$v.wares.Date.$error}">
                        <date-picker 
                            v-model="wares.Date" 
                            @blur="$v.wares.Date.$touch()" 
                            :class="{'is-invalid':$v.wares.Date.$error,
                                    'is-valid':!$v.wares.Date.$invalid}"
                             format="YYYY-MM-DD" display-format="dddd jDD jMMMM jYYYY" 
                             :auto-submit="true" placeholder="تاریخ دریافت کالا انتخاب کنید" 
                             input-class="form-control w-100" color="#b8221f" style="width:100%" :min='min'
                        />
                        <div class="hidden" :class="{'invalidFeedback':$v.wares.Date.$error}">لطفا این فیلد را پر کنید</div>
                    </div>
                    <div class="form-group mb-4 col-12">
                        <b-form-checkbox class="d-inline" size="lg" v-model="wares.Accept" value="notAccepted" unchecked-value="accepted"></b-form-checkbox>
                        <label class="pr-2">بعد از این تاریخ کالا را نمی پذیرم</label>
                    </div>
                    <button type="submit" :disabled="$v.$invalid" class="btn submit-btn">ثبت سفارش</button>
                </form>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import Header from '@/components/Header.vue';
import datePicker from 'vue-persian-datetime-picker';
import axios from 'axios'
import {required} from 'vuelidate/lib/validators'

export default {
    data() {
        return {
            previewimage: '',
            title: 'سفارش جدید',
            backlink: '/AllOrder',
            wares: {
                Title: '',
                Origin: '',
                Destination: "",
                Url: '',
                imagePath: '',
                Value: 1,
                Description: '',
                Date: '',
                Accept: 'accepted'
            },
            min: 0,
        }
    },
    methods: {
        onFileChange(e) {
            const file = e.target.files[0];
            this.previewimage = URL.createObjectURL(file);
            let formData = new FormData()
            formData.append('image', file);
            const path = '/api/uploadimage';
            axios.post(path, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                .then(resp => {
                    this.wares.imagePath = resp.data.filename
                    console.log(resp.data.filename)
                })
        },
        addWares(payload) {
            const path = '/api/neworder';
            const headers = {
                'Content-Type': 'multipart/form-data'
            }
            axios.post(path, payload, headers)
                .then(() => {
                    this.$router.push('/AllOrder');
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        onSubmit(evt) {
            evt.preventDefault();
            let Accept = true;
            if (this.wares.Accept == 'notAccepted') Accept = false;
            const payload = {
                Title: this.wares.Title,
                Origin: this.wares.Origin,
                Destination: this.wares.Destination,
                Url: this.wares.Url,
                imagePath: this.wares.imagePath,
                Value: this.wares.Value,
                Description: this.wares.Description,
                Date: this.wares.Date,
                Accept, // property shorthand
            };
            this.addWares(payload);
            this.initForm();
        },
        initForm() {
            this.wares.Title = '';
            this.wares.Origin = '';
            this.wares.Destination = '';
            this.wares.Url = '';
            this.wares.imagePath = '';
            this.wares.Value = 1;
            this.wares.Description = '';
            this.wares.Date = '';
            this.wares.Accept = [];
        },
        getMinData() {
            var todayDate = new Date().toISOString().slice(0, 10);
            this.min = todayDate
        },
    },
    created() {
        this.getMinData();
    },
    components: {
        Header,
        datePicker,
    },
    validations: {
        wares: {
            Title: {
                required
            },
            Origin: {
                required
            },
            Destination: {
                required
            },
            Url: {
                required
            },
            Description: {
                required
            },
            Date: {
                required
            },
        }
    }
}
</script>

<style>
textarea {
    width: 100%;
    min-height: 90px;
}

.new-order {
    padding: 15px 0;
}

.control-box {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

#preview {
    display: flex;
    justify-content: center;
    align-items: center;
}

#preview img {
    max-width: 80%;
    height: auto;
    padding: 20px 0;
}

.custom-file-label::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    z-index: 3;
    width: 100%;
    display: block;
    height: calc(1.5em + .75rem);
    padding: .375rem .75rem;
    line-height: 1.5;
    color: #495057;
    content: "انتخاب عکس";
    text-align: center;
    background-color: #e9ecef;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
}

.custom-file-label {
    border: none;
}
</style>
