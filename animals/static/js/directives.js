var petTrackerDirectives = angular.module('petTrackerDirectives', [])

petTrackerDirectives
    .directive('petList', [
        '$q',
        'PetTrackerFactory',
        function($q, PetTrackerFactory){
            return {
                restrict: 'E',
                templateUrl: "/static/js/templates/pet_list.html",
                replace: true,
                link: function(scope){
                    scope.ordering = "id";
                    scope.order = function(prop){
                        scope.ordering = scope.ordering == prop ? "-" + prop : prop
                    }

                    scope.filterAnimal = function(pet){
                        return pet.breed.animal.showing;
                    }

                    var animalsPromise = PetTrackerFactory.readAnimals().then(
                        function(promise){scope.animals = promise.data.results}
                    );
                    var breedsPromise = PetTrackerFactory.readBreeds().then(
                        function(promise){scope.breeds = promise.data.results}
                    );
                    var petsPromise = PetTrackerFactory.readPets().then(
                        function(promise){scope.pets = promise.data.results}
                    );

                    $q.all([animalsPromise, breedsPromise, petsPromise]).then(function(){
                        _.each(scope.animals, function(animal){
                            animal.showing = true;
                            animal.breeds = _.where(scope.breeds, {animal: animal.id});
                            _.each(animal.breeds, function(breed){
                                breed.animal = animal;
                                breed.pets = _.where(scope.pets, {breed: breed.id});
                                _.each(breed.pets, function(pet){
                                    pet.breed = breed;
                                });
                            });
                        });
                    });

                    scope.showPetDetails = function(pet){
                        scope.focusedPet = pet;
                    }
                }
            }
        }
    ])
    .directive('petForm', [
        'PetTrackerFactory',
        function(PetTrackerFactory){
            return {
                restrict: 'E',
                templateUrl: "/static/js/templates/pet_form.html",
                replace: true,
                scope: {
                    animals: '=',
                    addingPet: '=',
                },
                link: function(scope){
                    scope.clearForm = function(){
                        scope.form = {
                            pet: {},
                            errors: {}
                        }
                    }
                    scope.clearForm();

                    scope.cancelAddingPet = function(){
                        scope.addingPet = false;
                        scope.clearForm();
                    }
                }
            }
        }
    ])
    .directive('petDetails', ['PetTrackerFactory',
        function(PetTrackerFactory){
            return {
                restrict: 'E',
                templateUrl: "/static/js/templates/pet_details.html",
                replace: true,
                scope: {
                    pets: '=',
                    pet: '=',
                },
                link: function(scope){
                    scope.verifyDelete = function(){
                        scope.deletingPet = true;
                    }
                    scope.cancelDelete = function(){
                        scope.deletingPet = false;
                        scope.deleteVerification = null;
                    }
                    scope.deletePet = function(){
                        var removeObject = function(list, properties){
                            if (!list) return;
                            var objectIndex = _.indexOf(list, _.findWhere(list, properties));
                            list.splice(objectIndex, 1);
                        }

                        PetTrackerFactory.deletePet(scope.pet.id).then(
                            function(promise){
                                removeObject(scope.pets, {id: scope.pet.id})
                                scope.cancelDelete();
                                scope.pet = null;
                            }
                        );
                    }
                }
            }
        }
    ]);
