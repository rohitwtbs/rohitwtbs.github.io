<template>
<div class="technicalSkills">
    <h1 class="">Technical Skills</h1>
    <div class="skillText">
          <ul>
        <li>
            <div class="skillType"><b>Primary:</b></div>
            <div class="skillDescription">Node.js, Javascript, DynamoDb, ExpressJs, Diango(novice), Python(novice), Vue.js</div>
        </li>
    </ul>
    </div>
    
  

</div>
  
</template>

<script>
export default {
    name: 'TechnicalSkills',
    props: {
        msg: String
    }
}
</script>

<style>
h1 {
    text-align: left;
}
.skillType {
    float: left;
}
.skillDescription {
    float: right;
}
.skillText {
     margin-top: 2px;
    border-top: 5px solid green;
}
</style>