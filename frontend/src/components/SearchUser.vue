<template>
    <div class="box">
				<form name="search">
					<input type="text" class="input" name="txt" onmouseout="this.value = ''; this.blur();">
				</form>
				<i class="material-icons">
						search
				</i>
			</div>
</template>

<script>
    export default {
        name: 'SearchUser',
        data() {
            return {
                username: '',
            }
        },
    }
</script>

<style scoped>
.box{
    position: relative;
}

.input {
    padding: 10px;
    width: 40px;
    height: 40px;
    background: none;
    border: 4px solid #2c3e50;
    border-radius: 50px;
    box-sizing: border-box;
    font-family: "Montserrat";
    font-size: 16px;
    color: #2c3e50;
    outline: none;
    transition: .5s;
}
.box:hover input{
    width: 350px;
    background: #87CEEB;
    border-radius: 10px;
}
.box i{
    position: absolute;
    top: 50%;
    right: 15px;
    transform: translate(30%,-50%);
    font-size: 26px;
    color: #2c3e50;
    transition: .2s;
}
.box:hover i{
    opacity: 0;
    z-index: -1;
}

/* YouTube icon */
#ytb {
  height: 50px;
  width: 50px;
  text-align: center;
  line-height: 52px;
  border: 2px solid transparent;
  color: #FF7F50;
  font-size: 25px;
  transition: 0.3s;
}

#ytb:hover{
  border-radius: 50%;
  border-color: #FF7F50;
  box-shadow: 0 0 10px #FF7F50;
}
</style>