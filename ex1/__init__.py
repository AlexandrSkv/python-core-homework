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

    for categories_ids in mapping["categoryIdsSorted"]:
        result.append(
            {
            "id": "category-" + categories_ids,
            "text": mapping["categories"][categories_ids]["name"],
            "items": id_to_name(mapping["categories"][categories_ids]["roleIds"])
            }
        )
   
    return {"categories":result}
