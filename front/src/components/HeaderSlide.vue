<template>
<div>
    <header class="header">
        <h1>{{ title }}</h1>
        <button @click="headerToggle" class="modal-toggle"><i class="far fa-sliders-h"></i></button>
        <vue-slide-up-down :active="inputs" :duration="400">
            <div>
                <div class="form-group mt-3">
                    <input type="text" class="form-control" placeholder="مبدا">
                </div>
                <div class="form-group m-0">
                    <input type="text" class="form-control" placeholder="مقصد">
                </div>
            </div>
        </vue-slide-up-down>
    </header>
</div>
</template>

<script>
import VueSlideUpDown from 'vue-slide-up-down'

export default {
    components: {
        VueSlideUpDown
    },
    props: ['title'],
    data: () => ({
        inputs: false,
        rotate: false
    }),
    methods: {
        headerToggle() {
            this.inputs = !this.inputs;
            this.rotate = !this.rotate;
        }
    }
}
</script>

<style>
.header {
    text-align: center;
    padding: 20px;
    background: #b8221f;
    background: linear-gradient(to left, #b8221f, #e64135);
    color: #fff;
    margin: 0 -15px;
    position: relative;
}

.header h1 {
    font-size: 18px;
    font-weight: 600;
    margin: 0;
    padding-top: 5px;
}
</style>
