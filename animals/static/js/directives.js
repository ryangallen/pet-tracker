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
                        if (pet.breed.animal) return pet.breed.animal.showing;
                        return false;
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
                    pets: '=',
                },
                link: function(scope){
                    scope.clearForm = function(){
                        scope.form = {
                            pet: {},
                            errors: {}
                        }
                    }
                    scope.clearForm();

                    scope.cancelNewPet = function(){
                        scope.addingPet = false;
                        scope.clearForm();
                    }

                    scope.back = function(){
                        if (scope.form.pet.breed)
                            scope.form.pet.breed = null;
                        else if (scope.form.pet.animal)
                            scope.form.pet.animal = null;
                    }

                    scope.saveNewPet = function(){
                        scope.form.errors = {};
                        if (!scope.form.pet.name)
                            scope.form.errors.name = ["A name is required"];
                        if (scope.form.pet.name.length > 30)
                            scope.form.errors.name = ["The name is can be no more than 30 characters"];
                        if (!scope.form.pet.birthday)
                            scope.form.errors.birthday = ["A birthday is required"];
                        if (!_.isEmpty(scope.form.errors)) return;

                        PetTrackerFactory.createPet({
                            name: scope.form.pet.name,
                            breed: scope.form.pet.breed.id,
                            birthday: scope.form.pet.birthday
                                           .toISOString().slice(0, 10),
                        }).then(
                            function(promise){
                                promise.data.animal = scope.form.pet.animal;
                                promise.data.breed = scope.form.pet.breed;
                                promise.data.showing = true;

                                scope.pets.push(promise.data);
                                scope.addingPet = false;
                                scope.clearForm();
                            },
                            function(promise){
                                scope.form.errors = promise.data
                            }
                        );
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
