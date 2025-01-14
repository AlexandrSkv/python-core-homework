def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    # put your code here
    def id_to_name(roles_list):
        result = []
        for role_id in roles_list:
            result.append(
               {
               "id": role_id,
               "text": mapping["roles"][role_id]["name"]
                }
            )
        return result
        
    result = []

    for category_id in mapping["categoryIdsSorted"]:
        result.append(
            {
            "id": "category-" + category_id,
            "text": mapping["categories"][category_id]["name"],
            "items": id_to_name(mapping["categories"][category_id]["roleIds"])
            }
        )
   
    return {"categories":result}
