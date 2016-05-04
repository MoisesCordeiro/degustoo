(function(){angular.module('RestauranteAPP',[]).config(['$httpProvider','$interpolateProvider',function($httpProvider,$interpolateProvider){$interpolateProvider.startSymbol('[[');$interpolateProvider.endSymbol(']]');$httpProvider.defaults.xsrfHeaderName='X-CSRFToken';$httpProvider.defaults.xsrfCookieName='csrftoken';}]);}).call(this);(function(){angular.module('RestauranteAPP').controller('cardapioController',function($scope,cardapioAJAX){var reload;reload=function(restaurante_id){cardapioAJAX.listarCardapios(restaurante_id).success(function(data){$scope.lista_cardapio=data;});};this.novoCardapio=function(restaurante_id,dados){cardapioAJAX.novoCardapio(restaurante_id,dados).success(function(data){reload(restaurante_id);}).error(function(data){console.log(data);});};this.listarCardapios=function(restaurante_id){cardapioAJAX.listarCardapios(restaurante_id).success(function(data){reload(restaurante_id);}).error(function(data){console.log(data);});};this.getCardapio=function(restaurante_id,cardapio_id){cardapioAJAX.getCardapio(resturante_id,cardapio_id).success(function(data){console.log(data);}).error(function(data){console.log(data);});};this.editarCardapio=function(restaurante_id,cardapio_id,dados){cardapioAJAX.editarCardapio(restaurante_id,cardapio_id,dados).success(function(data){reload(restaurante_id);}).error(function(data){console.log(data);});};this.deletarCardapio=function(restaurante_id,cardapio_id){cardapioAJAX.deletarCardapio(restaurante_id,cardapio_id).success(function(data){reload(restaurante_id);}).error(function(data){console.log(data);});};});}).call(this);(function(){angular.module('RestauranteAPP').controller('subcardapioController',function($scope,subcardapioAJAX){var reload;reload=function(cardapio_id){subcardapioAJAX.listarSubcardapios(cardapio_id).success($scope.lista_subcardapio=data);};this.novoSubcardapio=function(cardapio_id,dados){subcardapioAJAX.novoSubcardapio(cardapio_id,dados).success(function(data){return reload(cardapio_id);}).error(function(data){return console.log(data);});};this.listarSubcardapios=function(cardapio_id){subcardapioAJAX.listarSubcardapios(cardapio_id).success(function(data){return reload(cardapio_id);}).error(function(data){return console.log(data);});};this.getSubcardapio=function(cardapio_id,subcardapio_id){subcardapioAJAX.getSubcardapio(cardapio_id,subcardapio_id).success(function(data){return console.log(data);}).error(function(data){return console.log(data);});};this.editarSubcardapio=function(cardapio_id,subcardapio_id,dados){subcardapioAJAX.editarSubcardapio(cardapio_id,subcardapio_id,dados).success(function(data){return reload(cardapio_id);}).error(function(data){return console.log(data);});};this.deletarSubcardapio=function(cardapio_id,subcardapio_id){subcardapioAJAX.deletarSubcardapio(cardapio_id,subcardapio_id).success(function(data){return reload(cardapio_id);}).error(function(data){return console.log(data);});};});}).call(this);(function(){angular.module('RestauranteAPP').controller('opcaoController',function($scope,opcaoAJAX){var reload;reload=function(cardapio_id){opcaoAJAX.listarOpcoes(cardapio_id).success($scope.lista_opcao=data);};this.novaOpcao=function(cardapio_id,dados){opcaoAJAX.novaOpcao(cardapio_id,dados).success(function(data){reload(cardapio_id);}).error(function(data){console.log(data);});};this.listarOpcoes=function(cardapio_id){opcaoAJAX.listarOpcoes(cardapio_id).success(function(data){reload(cardapio_id);}).error(function(data){console.log(data);});};this.getOpcao=function(cardapio_id,opcao_id){opcaoAJAX.getOpcao(cardapio_id,opcao_id).success(function(data){console.log(data);}).error(function(data){console.log(data);});};this.editarOpcao=function(cardapio_id,opcao_id,dados){opcaoAJAX.editarOpcao(cardapio_id,opcao_id,dados).success(function(data){reload(cardapio_id);}).error(function(data){console.log(data);});};this.deletarOpcao=function(cardapio_id,opcao_id){opcaoAJAX.deletarOpcao(cardapio_id,opcao_id).success(function(data){reload(cardapio_id);}).error(function(data){console.log(data);});};});}).call(this);(function(){angular.module('RestauranteAPP').controller('itemCardapioController',function($scope,itemCardapioAJAX){var reload;reload=function(cardapio_id){itemCardapioAJAX.listarItens(cardapio_id).success(function(data){$scope.lista_item_cardapio=data;$scope.novoItem.nome="";$scope.novoItem.preco="";});};this.novoItem=function(cardapio_id){itemCardapioAJAX.novoItem(cardapio_id).success(function(data){reload(cardapio_id);}).error(function(data){console.log(data);});};this.listarItens=function(cardapio_id){itemCardapioAJAX.listarItens(cardapio_id).success(function(data){reload(cardapio_id);}).error(function(data){console.log(data);});};this.getItem=function(cardapio_id,item_id){itemCardapioAJAX.getItem(cardapio_id,item_id).success(function(data){}).error(function(data){});};this.editarItem=function(cardapio_id,item_id,dados){itemCardapioAJAX.editarItem(cardapio_id,item_id,dados).success(function(data){}).error(function(data){});};this.deletarItem=function(cardapio_id,item_id){itemCardapioAJAX.deletarItem(cardapio_id,item_id).success(function(data){reload(cardapio_id);}).error(function(data){console.log(data);});};});}).call(this);(function(){angular.module('RestauranteAPP').controller('itemSubcardapioController',function($scope,itemSubcardapioAJAX){var reload;reload=function(subcardapio_id){itemSubcardapioAJAX.listarItens(subcardapio_id).success(function(data){$scope.lista_item_subcardapio=data;$scope.novoItem.nome="";$scope.novoItem.preco="";});};this.novoItem=function(subcardapio_id){itemSubcardapioAJAX.novoItem(subcardapio_id).success(function(data){reload(subcardapio_id);}).error(function(data){console.log(data);});};this.listarItens=function(subcardapio_id){itemSubcardapioAJAX.listarItens(subcardapio_id).success(function(data){reload(subcardapio_id);}).error(function(data){console.log(data);});};this.getItem=function(subcardapio_id,item_id){itemSubcardapioAJAX.getItem(subcardapio_id,item_id).success(function(data){}).error(function(data){});};this.editarItem=function(subcardapio_id,item_id,dados){itemSubcardapioAJAX.editarItem(subcardapio_id,item_id,dados).success(function(data){}).error(function(data){});};this.deletarItem=function(subcardapio_id,item_id){itemSubcardapioAJAX.deletarItem(subcardapio_id,item_id).success(function(data){reload(subcardapio_id);}).error(function(data){console.log(data);});};});}).call(this);(function(){angular.module('RestauranteAPP').controller('itemOpcaoController',function($scope,itemOpcaoAJAX){var reload;reload=function(opcao_id){itemOpcaoAJAX.listarItens(opcao_id).success(function(data){$scope.lista_item_opcao=data;$scope.novoItem.nome="";$scope.novoItem.preco="";});};this.novoItem=function(opcao_id){itemOpcaoAJAX.novoItem(opcao_id).success(function(data){reload(opcao_id);}).error(function(data){console.log(data);});};this.listarItens=function(opcao_id){itemOpcaoAJAX.listarItens(opcao_id).success(function(data){reload(opcao_id);}).error(function(data){console.log(data);});};this.getItem=function(opcao_id,item_id){itemOpcaoAJAX.getItem(opcao_id,item_id).success(function(data){}).error(function(data){});};this.editarItem=function(opcao_id,item_id,dados){itemOpcaoAJAX.editarItem(opcao_id,item_id,dados).success(function(data){}).error(function(data){});};this.deletarItem=function(opcao_id,item_id){itemOpcaoAJAX.deletarItem(opcao_id,item_id).success(function(data){reload(opcao_id);}).error(function(data){console.log(data);});};});}).call(this);(function(){angular.module('RestauranteAPP').directives('listaCardapio',function(){return{restrict:'E',templateUrl:'/static/restaurante/js/application/templates/lista-cardapio.html',controller:'cardapioController',controllerAs:'cardapio_controller'};});}).call(this);(function(){angular.module('RestauranteAPP').directives('listaSubcardapio',function(){return{restrict:'E',templateUrl:'/static/restaurante/js/application/templates/lista-subcardapio.html',controller:'subcardapioController',controllerAs:'subcardapio_controller'};});}).call(this);(function(){angular.module('RestauranteAPP').directives('listaOpcao',function(){return{restrict:'E',templateUrl:'/static/restaurante/js/application/templates/lista-opcao.html',controller:'opcaoController',controllerAs:'opcao_controller'};});}).call(this);(function(){angular.module('RestauranteAPP').directives('listaItemCardapio',function(){return{restrict:'E',templateUrl:'/static/restaurante/js/application/templates/lista-item-cardapio.html',controller:'itemCardapioController',controllerAs:'item_cardapio_controller'};});}).call(this);(function(){angular.module('RestauranteAPP').directives('listaItemSubcardapio',function(){return{restrict:'E',templateUrl:'/static/restaurante/js/application/templates/lista-item-subcardapio.html',controller:'itemSubcardapioController',controllerAs:'item_subcardapio_controller'};});}).call(this);(function(){angular.module('RestauranteAPP').directives('listaItemOpcao',function(){return{restrict:'E',templateUrl:'/static/restaurante/js/application/templates/lista-item-opcao.html',controller:'itemOpcaoController',controllerAs:'item_opcao_controller'};});}).call(this);(function(){angular.module('RestauranteAPP').factory('cardapioAJAX',function($http){var _deletarCardapio,_editarCardapio,_getCardapio,_listarCardapios,_novoCardapio;_novoCardapio=function(restaurante_id,dados){return $http({method:'POST',url:'/ajax/restaurante/'+restaurante_id+'/cardapio/',data:dados});};_listarCardapios=function(restaurante_id){return $http({method:'GET',url:'/ajax/restaurante/'+restaurante_id+'/cardapio/'});};_getCardapio=function(restaurante_id,cardapio_id){return $http({method:'GET',url:'/ajax/restaurante/'+restaurante_id+'/cardapio/'+cardapio_id+'/'});};_editarCardapio=function(restarante_id,cardapio_id,dados){return $http({method:'PUT',url:'/ajax/restaurante/'+restaurante_id+'/cardapio/'+cardapio_id+'/',data:dados});};_deletarCardapio=function(restaurante_id,cardapio_id){return $http({method:'DELETE',url:'/ajax/restaurante/'+restaurante_id+'/cardapio/'+cardapio_id+'/'});};return{novoCardapio:_novoCardapio,listarCardapios:_listarCardapios,getCardapio:_getCardapio,editarCardapio:_editarCardapio,deletarCardapio:_deletarCardapio};});}).call(this);(function(){angular.module('RestauranteAPP').factory('subcardapioAJAX',function($http){var _deletarSubcardapio,_editarSubcardapio,_getSubcardapio,_listarSubcardapios,_novoSubcardapio;_novoSubcardapio=function(cardapio_id,dados){return $http({method:'POST',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/',data:dados});};_listarSubcardapios=function(cardapio_id){return $http({method:'GET',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'});};_getSubcardapio=function(cardapio_id,subcardapio_id){return $http({method:'GET',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'+subcardapio_id+'/'});};_editarSubcardapio=function(cardapio_id,subcardapio_id,dados){return $http({method:'PUT',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'+subcardapio_id+'/',data:dados});};_deletarSubcardapio=function(cardapio_id,subcardapio_id){return $http({method:'DELETE',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/subcardapio/'+subcardapio_id+'/'});};return{novoSubcardapio:_novoSubcardapio,listarSubcardapios:_listarSubcardapios,getSubcardapio:_getSubcardapio,editarSubcardapio:_editarSubcardapio,deletarSubcardapio:_deletarSubcardapio};});}).call(this);(function(){angular.module('RestauranteAPP').factory('opcaoAJAX',function($http){var _deletarOpcao,_editarOpcao,_getOpcao,_listarOpcoes,_novoOpcao;_novoOpcao=function(cardapio_id,dados){return $http({method:'POST',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/',data:dados});};_listarOpcoes=function(cardapio_id){return $http({method:'GET',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'});};_getOpcao=function(cardapio_id,opcao_id){return $http({method:'GET',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/'});};_editarOpcao=function(cardapio_id,opcao_id,dados){return $http({method:'PUT',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/',data:dados});};_deletarOpcao=function(cardapio_id,opcao_id){return $http({method:'DELETE',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/opcao/'+opcao_id+'/'});};return{novaOpcao:_novaOpcao,listarOpcoes:_listarOpcoes,getOpcao:_getOpcao,editarOpcao:_editarOpcao,deletarOpcao:_deletarOpcao};});}).call(this);(function(){angular.module('RestauranteAPP').factory('itemCardapioAJAX',function($http){var _deletarItem,_editarItem,_getItem,_listarItens,_novoItem;_novoItem=function(cardapio_id,dados){return $http({method:'POST',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/item/',data:dados});};_listarItens=function(cardapio_id){return $http({method:'GET',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/item/'});};_getItem=function(cardapio_id,item_id){return $http({method:'GET',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/item/'+item_id+'/'});};_editarItem=function(cardapio_id,item_id,dados){return $http({method:'PUT',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/item/'+item_id+'/',data:dados});};_deletarItem=function(cardapio_id,item_id){return $http({method:'DELETE',url:'/ajax/restaurante/cardapio/'+cardapio_id+'/item/'+item_id+'/'});};return{novoItem:_novoItem,editarItem:_editarItem,getItem:_getItem,listarItens:_listarItens,deletarItem:_deletarItem};});}).call(this);(function(){angular.module('RestauranteAPP').factory('itemSubcardapioAJAX',function($http){var _deletarItem,_editarItem,_getItem,_listarItens,_novoItem;_novoItem=function(subcardapio_id,dados){return $http({method:'POST',url:'/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/',data:dados});};_listarItens=function(subcardapio_id){return $http({method:'GET',url:'/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/'});};_getItem=function(subcardapio_id,item_id){return $http({method:'GET',url:'/ajax/restaurante/subcardapio/'+cardapio_id+'/item/'+item_id+'/'});};_editarItem=function(subcardapio_id,item_id,dados){return $http({method:'PUT',url:'/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/'+item_id+'/',data:dados});};_deletarItem=function(subcardapio_id,item_id){return $http({method:'DELETE',url:'/ajax/restaurante/subcardapio/'+subcardapio_id+'/item/'+item_id+'/'});};return{novoItem:_novoItem,editarItem:_editarItem,getItem:_getItem,listarItens:_listarItens,deletarItem:_deletarItem};});}).call(this);(function(){angular.module('RestauranteAPP').factory('itemOpcaoAJAX',function($http){var _deletarItem,_editarItem,_getItem,_listarItens,_novoItem;_novoItem=function(opcao_id,dados){return $http({method:'POST',url:'/ajax/restaurante/opcao/'+opcao_id+'/item/',data:dados});};_listarItens=function(opcao_id){return $http({method:'GET',url:'/ajax/restaurante/opcao/'+opcao_id+'/item/'});};_getItem=function(opcao_id,item_id){return $http({method:'GET',url:'/ajax/restaurante/opcao/'+opcao_id+'/item/'+item_id+'/'});};_editarItem=function(opcao_id,item_id,dados){return $http({method:'PUT',url:'/ajax/restaurante/opcao/'+opcao_id+'/item/'+item_id+'/',data:dados});};_deletarItem=function(opcao_id,item_id){return $http({method:'DELETE',url:'/ajax/restaurante/opcao/'+opcao_id+'/item/'+item_id+'/'});};return{novoItem:_novoItem,editarItem:_editarItem,getItem:_getItem,listarItens:_listarItens,deletarItem:_deletarItem};});}).call(this);