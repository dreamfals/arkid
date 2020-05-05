"""
Define OrgClient
"""
from arkid_client.authorizers import BasicAuthorizer
from arkid_client.base import BaseClient
from arkid_client.exceptions import OrgAPIError
from arkid_client.response import ArkIDHTTPResponse


class OrgClient(BaseClient):
    """
    组织管理客户端，用于与 ArkID 服务端组织管理相关
    接口的访问操作。

    **Methods**

    *  :py:meth:`.query_own_org`
    *  :py:meth:`.query_org`
    *  :py:meth:`.create_org`
    *  :py:meth:`.delete_org`
    *  :py:meth:`.update_org`
    *  :py:meth:`.query_orguser`
    *  :py:meth:`.add_orguser`
    *  :py:meth:`.delete_orguser`
    *  :py:meth:`.query_orguser`
    *  :py:meth:`.update_orguser`
    *  :py:meth:`.get_org_invitation_key`
    *  :py:meth:`.refresh_org_invitation_key`
    *  :py:meth:`.view_org_by_invitation_key`
    *  :py:meth:`.join_org_by_invitation_key`
    """
    allowed_authorizer_types = [BasicAuthorizer]
    error_class = OrgAPIError
    default_response_class = ArkIDHTTPResponse

    def __init__(self, base_url, authorizer=None, **kwargs):
        BaseClient.__init__(self, base_url, "org", authorizer=authorizer, **kwargs)

    def query_own_org(self, **params):
        """
        查询用户所在的组织
        (``GET /siteapi/v1/org/``)

        **Parameters**:

            ``role`` (*str*)
              在组织内的角色

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> orgs = oc.query_own_org(role='admin')
        >>> for org in orgs:
        >>>     print(org['oid'], 'name: '
        >>>           ,org['name'])
        """
        self.logger.info("正在调用 OrgClient.query_own_org() 接口与 ArkID 服务端进行交互")
        return self.get(path='', params=params)

    def query_org(self, oid: str):
        """
        查看指定组织的信息
        (``GET /siteapi/v1/org/<oid>/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> org = oc.query_org(oid)
        >>> print(org['oid'], 'name: '
        >>>       ,org['name'])
        """
        self.logger.info("正在调用 OrgClient.query_org() 接口与 ArkID 服务端进行交互")
        return self.get(path='{}/'.format(oid))

    def create_org(self, json_body: dict):
        """
        创建组织
        (``POST /siteapi/v1/org/``)

        **Parameters**:

            ``json_body`` (*dict*)
              组织的元信息， 参数详情请参考接口文档

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> org_data = {
        >>>   "name": "example",
        >>> }
        >>> org = oc.create_org(org_data)
        >>> print(org['oid'], 'name: '
        >>>       ,org['name'])

        **External Documentation**

        关于 `组织的元数据 \
        <https://arkid.docs.apiary.io/#reference/org/0/1>`_
        详情请参阅API文档。
        """
        self.logger.info("正在调用 OrgClient.create_org() 接口与 ArkID 服务端进行交互")
        return self.post(path='', json_body=json_body)

    def delete_org(self, oid: str):
        """
        删除指定组织的信息
        (``DELETE /siteapi/v1/org/<oid>/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> oc.delete_org(oid)
        """
        self.logger.info("正在调用 OrgClient.delete_org() 接口与 ArkID 服务端进行交互")
        return self.delete(path='{}/'.format(oid))

    def update_org(self, oid: str, json_body: dict):
        """
        修改指定组织的信息
        (``PATCH /siteapi/v1/org/<oid>/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``json_body`` (*dict*)
              组织的元信息， 参数详情请参考接口文档

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> org_data = {
        >>>   "name": "example",
        >>> }
        >>> org = oc.update_org(oid, org_data)
        >>> print(org['oid'], 'name: '
        >>>       ,org['name'])

        **External Documentation**

        关于 `组织的元数据 \
        <https://arkid.docs.apiary.io/#reference/org/1/2>`_
        详情请参阅API文档。
        """
        self.logger.info("正在调用 OrgClient.update_org() 接口与 ArkID 服务端进行交互")
        return self.patch(path='{}/'.format(oid), json_body=json_body)

    def query_orguser_list(self, oid: str, **params):
        """
        查看特定组织的成员信息
        (``GET /siteapi/v1/org/<oid>/user/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``page`` (*int*)
              用于分页，*Default: 1*

            ``page_size`` (*int*)
              指定分页大小，*Default: 30*

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> org = oc.query_orguser_list(oid)
        >>> print(org['oid'], 'name: '
        >>>       ,org['name'])
        """
        self.logger.info("正在调用 OrgClient.query_orguser_list() 接口与 ArkID 服务端进行交互")
        return self.get(path='{}/user/'.format(oid), params=params)

    def add_orguser(self, oid: str, usernames: list):
        """
        向指定组织中添加成员
        (``PATCH /siteapi/v1/org/<oid>/user/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``usernames`` (*list*)
              用户的唯一标识组成的列表

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> usernames = [
        >>>     'username1',
        >>>     'username2',
        >>>         ...
        >>>     'usernamen'
        >>> ]
        >>> org = oc.add_orguser(oid, usernames)
        >>> print(org['oid'], 'name: '
        >>>       ,org['name'])
        """
        self.logger.info("正在调用 OrgClient.add_orguser() 接口与 ArkID 服务端进行交互")
        json_body = {'subject': 'add', 'usernames': usernames}
        return self.patch(path='{}/user/'.format(oid), json_body=json_body)

    def delete_orguser(self, oid: str, usernames: list):
        """
        从指定组织中移除成员
        (``PATCH /siteapi/v1/org/<oid>/user/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``usernames`` (*list*)
              用户的唯一标识组成的列表

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> usernames = [
        >>>     'username1',
        >>>     'username2',
        >>>         ...
        >>>     'usernamen'
        >>> ]
        >>> org = oc.delete_orguser(oid, usernames)
        >>> print(org['oid'], 'name: '
        >>>       ,org['name'])
        """
        self.logger.info("正在调用 OrgClient.delete_orguser() 接口与 ArkID 服务端进行交互")
        json_body = {'subject': 'delete', 'usernames': usernames}
        return self.patch(path='{}/user/'.format(oid), json_body=json_body)

    def query_orguser(self, oid: str, username: str):
        """
        查看指定组织的指定成员的信息
        (``GET /siteapi/v1/org/<oid>/user/<username>/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``username`` (*str*)
              用户唯一标识

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> user = oc.query_orguser(oid, username)
        >>> print('user is', user)
        """
        self.logger.info("正在调用 OrgClient.query_orguser() 接口与 ArkID 服务端进行交互")
        return self.get(path='{}/user/{}/'.format(oid, username))

    def update_orguser(self, oid: str, username: str, json_body: dict):
        """
        编辑指定组织的指定成员的信息
        (``PATCH /siteapi/v1/org/<oid>/user/<username>/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``username`` (*str*)
              用户唯一标识

            ``json_body`` (*dict*)

                ``email`` (*str*)
                  成员邮箱

                ``employee_number`` (*str*)
                  成员工号

                ``position`` (*str*)
                  成员职位

                ``hiredate`` (*str*)
                  成员雇佣日期

                ``remark`` (*str*)
                  成员备注

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> user_data = {
        >>>   "email": "example@org.com",
        >>> }
        >>> user = oc.update_orguser(oid, username, user_data)
        >>> print(user['id'], 'name: '
        >>>       ,user['name'])

        **External Documentation**

        关于 `成员的元数据 \
        <https://arkid.docs.apiary.io/#reference/org/3/1>`_
        详情请参阅API文档。
        """
        self.logger.info("正在调用 OrgClient.update_orguser() 接口与 ArkID 服务端进行交互")
        return self.patch(path='{}/user/{}/'.format(oid, username), json_body=json_body)

    def get_org_invitation_key(self, oid: str):
        """
        获取指定组织邀请用的最新的密钥
        (``GET /siteapi/v1/org/<oid>/invitation/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> key = oc.get_org_invitation_key(oid)
        >>> print('key: ', key)
        """
        self.logger.info("正在调用 OrgClient.get_org_invitation_key() 接口与 ArkID 服务端进行交互")
        return self.get(path='{}/invitation/'.format(oid))

    def refresh_org_invitation_key(self, oid: str):
        """
        刷新指定组织邀请用的最新的密钥
        (``PUT /siteapi/v1/org/<oid>/invitation/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> key = oc.refresh_org_invitation_key(oid)
        >>> print('key: ', key)
        """
        self.logger.info("正在调用 OrgClient.get_org_invitation_key() 接口与 ArkID 服务端进行交互")
        return self.put(path='{}/invitation/'.format(oid))

    def view_org_by_invitation_key(self, oid: str, invite_link_key: str):
        """
        使用邀请密钥查看指定组织的信息
        (``GET /siteapi/v1/org/<oid>/invitation/<invite_link_key>/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``invite_link_key`` (*str*)
              组织邀请密钥

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> org = oc.view_org_by_invitation_key(oid, invite_link_key)
        >>> print('org: ', org)
        """
        self.logger.info("正在调用 OrgClient.view_org_by_invitation_key() 接口与 ArkID 服务端进行交互")
        return self.get(path='{}/invitation/{}/'.format(oid, invite_link_key))

    def join_org_by_invitation_key(self, oid: str, invite_link_key: str):
        """
        使用邀请密钥加入指定组织
        (``POST /siteapi/v1/org/<oid>/invitation/<invite_link_key>/``)

        **Parameters**:

            ``oid`` (*str*)
              组织的唯一标识

            ``invite_link_key`` (*str*)
              组织邀请密钥

        **Examples**

        >>> oc = arkid_client.OrgClient(...)
        >>> org = oc.join_org_by_invitation_key(oid, invite_link_key)
        >>> print('org: ', org)
        """
        self.logger.info("正在调用 OrgClient.join_org_by_invitation_key() 接口与 ArkID 服务端进行交互")
        return self.post(path='{}/invitation/{}/'.format(oid, invite_link_key))
