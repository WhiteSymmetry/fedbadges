from setuptools import setup
requires = [
        'tahrir-api',
        'fedmsg']

long_description = file("readme.rst").read().strip()
setup(
        name='fedbadges',
        version='0.1.0',
        description='fedmsg consumer for awarding open badges',
        long_description=long_description,
        author='Ross Delinger',
        author_email='rdelinge@redhat.com',
        url='https://github.com/rossdylan/fedbages',
        install_requires=requires,
        packages=[
            'fedbadges.consumers',
            'fedbadges.commands'],
        zip_safe=False,
        entry_points={
            'console_scripts': [
                "fedmsg-badges=fedbadges.commands.badges:badges"],
            'moksha.consumer': [
                "fedmsg-badges=fedbadges.consumers.ExampleBadge:ExampleBadgessConsumer"]},)