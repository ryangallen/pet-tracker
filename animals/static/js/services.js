var petTrackerServices = angular.module('petTrackerServices', ['ngResource'])

petTrackerServices.factory('PetTrackerFactory', [
    '$http',
    function($http){

        var endpoints = {
            animals: "/api/animals/",
            breeds: "/api/breeds/",
            pets: "/api/pets/",
        }

        return {
            readAnimals: function(symbols){
                return $http.get(endpoints.animals);
            },
            readBreeds: function(symbols){
                return $http.get(endpoints.breeds);
            },
            readPets: function(symbols){
                return $http.get(endpoints.pets);
            },
        }
    }
]);
