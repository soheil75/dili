<template>
<div>
    <header class="header">
        <router-link class="back-btn" :to="link">
            <i class="far fa-angle-left ver-middle"></i>
        </router-link>
        <h1>{{title}}</h1>
    </header>
</div>
</template>

<script>
export default {
    props: ['link', 'title']
}
</script>

<style>
.back-btn {
    font-size: 18px;
    color: #fff;
    padding: 10px;
    position: absolute;
    left: 20px;
    top: 13px;
}

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
