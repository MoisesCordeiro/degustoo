(function(){angular.module('main',[]).config(['$httpProvider','$interpolateProvider',function($httpProvider,$interpolateProvider){$interpolateProvider.startSymbol('[[');$interpolateProvider.endSymbol(']]');$httpProvider.defaults.xsrfHeaderName='X-CSRFToken';$httpProvider.defaults.xsrfCookieName='csrftoken';}]).services.directives.controller('cardapioController',function($http,$scope){this.addCardapio=function(){};this.listarCardapios=function(){};this.getCardapio=function(){};this.editarCardapio=function(){};this.deletarCardapio=function(){};}).controller('itemCardapioController',function($http,$scope,itemCardapioAJAX){(function(cardapio_id){itemCardapioAJAX.getItens(card_id).success(function(data){$scope.itens=data.novoItem.nome="".preco="";});});});}).call(this);