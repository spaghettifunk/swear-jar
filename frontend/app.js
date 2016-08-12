var swear = angular.module("swear", []);

swear.controller("swearCtrl", function($scope, $http) {
  $scope.euro_bjorn = 0;
  $scope.euro_alex = 0;
  $scope.euro_wang = 0;
  $scope.euro_patrick = 0;
  $scope.euro_dario = 0;
  $scope.euro_davide = 0;
  $scope.euro_rafael = 0;

  //a scope function to load the data.
   $scope.loadData = function () {
      $http.get('/')
      .success(function(data) {
         var response = JSON.parse(data);
           $scope.euro_bjorn = response.euro_bjorn;
           $scope.euro_alex = response.euro_alex;
           $scope.euro_wang = response.euro_wang;
           $scope.euro_patrick = response.euro_patrick;
           $scope.euro_dario = response.euro_dario;
           $scope.euro_davide = response.euro_davide;
           $scope.euro_rafael = response.euro_rafael;
      });
   };

});
