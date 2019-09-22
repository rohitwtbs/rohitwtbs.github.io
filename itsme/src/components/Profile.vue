<template>
    <div class="profile">
        <h1 class="">PROFILE SUMMARY</h1>
        <div class="profileText">
            <ul>
                  <li>
                      A result-oriented programmer who is passionate about learning high end
                computing fields and exploring new possibilities for their applications.
            </li>
            <li>
                Insightful knowledge of NodeJs, DynamoDb, Javascript.
            </li>
            <li>
                Seeking to enrich my technical & leadership skills by working on challenging
                 development projects with a team of
                motivated individuals who share the same passion of solving problems and ensuring time bound delivery.
            </li>
            </ul>
          
        </div>
    </div>
</template>
<script>
export default {
  name: 'Profile',
  props: {
    msg: String
  }
}
</script>

<style>
li {
    padding-left :1px;
    text-align: left;
}
/* .profileText{
    align-self: left;

} */
/* why is it not taking the style if given in class for h1 */
h1 {
    text-align: left;
}
.profileText {
    margin-top: 2px;
    border-top: 5px solid green;
}
</style>