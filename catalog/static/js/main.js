       var args = {'category': [], 'value': []};
        var search = {};


        function handle_filter(element) {
            let parts = element.id.split('_');
            let type = parts[0];
            let id = parts[1];
            if (!element.is_active) { // если is_active == False  то значит что элемент выбрали, иначе его нажали второй раз(тоесть убрали галочку
                args[type].push(id); //add ID in args with key Type
            } else {
                args[type].forEach((value, index) => {
                   if (value === id) {
                       args[type].splice(index, 1); // delete one(1) element by index
                   }
                });
            }
            element.is_active = !element.is_active;
        }
        function update() {
            let all_args = [];
            for (let [type, value] of Object.entries(args)){
                console.log(value, type);
                value.forEach((id) => {
                    all_args.push([type, id].join('='));
                })
            }
            document.location.search = all_args.join('&');
        }