       var args = {'category': [], 'attribute_value': []};
        var search = {};

//        function handle_search(data, type) {
//            search[type] = data.value;
//            document.location.search = search.join('=');
//
//        }

        function handle_filter(element) {
            let parts = element.id.split('_');
            let type = parts[0];
            let id = parts[1];
            if (!element.is_active) {
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