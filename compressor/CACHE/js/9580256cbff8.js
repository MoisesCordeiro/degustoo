(function(){angular.module('main',[]).config(['$httpProvider','$interpolateProvider',function($httpProvider,$interpolateProvider){$interpolateProvider.startSymbol('[[');$interpolateProvider.endSymbol(']]');$httpProvider.defaults.xsrfHeaderName='X-CSRFToken';$httpProvider.defaults.xsrfCookieName='csrftoken';}]).services.directives('listaItemCardapio',function(){var directive;return directive={restrict:'E',templateUrl:'/static/restaurante/js/application/templates/lista_itemMenu.html',controller:'itemCardapioController',controllerAs:'item_cardapio_controller'};}).controller('cardapioController',function($http,$scope){this.addCardapio=function(){};this.listarCardapios=function(){};this.getCardapio=function(){};this.editarCardapio=function(){};this.deletarCardapio=function(){};}).controller('itemCardapioController',function($http,$scope,itemCardapioAJAX){var reload;reload=function(cardapio_id){itemCardapioAJAX.getItens(card_id).success(function(data){$scope.itens=data;$scope.novoItem.nome="";$scope.novoItem.preco="";});};this.addItemCardapio=function(cardapio_id){itemCardapioAjax.novoItem(cardapio_id).success(function(data){this.reload(cardapio_id);}).error(function(data){console.log(data);});};this.listarItemCardapio=function(cardapio_id){itemCardapioAjax.listarItens(cardapio_id).success(function(data){this.reload(cardapio_id);}).error(function(data){console.log(data);});};this.getItemCardapio=function(){};this.editarItemCardapio=function(){};this.deletarItemCardapio=function(cardapio_id,item_id){itemCardapioAjax.deletarItem(cardapio_id,item_id).success(function(data){this.reload(cardapio_id);}).error(function(data){console.log(data);});};});}).call(this);